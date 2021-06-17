import sys
# import libraries
import pandas as pd 
import numpy as np

def load_data(messages_filepath, categories_filepath):
    """Function : Load and merge messages and categories datasets  """ 
    
    """Arguments :
    messages_filepath: string. Filepath for csv file containing messages dataset.
    categories_filepath: string. Filepath for csv file containing categories dataset.
    """
    """Returns : 
    df: dataframe. Dataframe containing merged content of messages and categories datasets.
    """
    ## read message dataset 
    messages = pd.read_csv(messages_filepath)
    ## read categories dataset
    categories = pd.read_csv(categories_filepath)
    ## merge the two datasets in dataframe
    df = pd.merge(messages,categories,on="id")
    return df

def clean_data(df):
    """Function : Clean dataframe by removing duplicates and converting categories from strings 
    to binary values."""
    
    """Arguments:
    df: dataframe. Dataframe containing merged content of messages and categories datasets."""
       
    """Returns:
    df: dataframe. Dataframe containing cleaned version of input dataframe.
    """
    categories = df.categories.str.split(";",expand=True)
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = []
    for ind in range(len(row)):
        category_colnames.append(row[ind])
    # rename the columns of `categories`
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
        
    df.drop('categories',axis=1,inplace = True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories],axis=1,join="inner")
    ## drop duplicated rows
    df.drop_duplicates(inplace=True)
    ## return cleaned dataframe
    return df


def save_data(df, database_filename):
    """Function : Save cleaned data into an SQLite database. """
    
    """Arguments:
    df: dataframe. Dataframe containing cleaned version of merged message and categories data.
    database_filename: string. Filename for output database.
    """
       
    """Returns :
    None
    """
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///disaster.db')
    df.to_sql('disaster', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()