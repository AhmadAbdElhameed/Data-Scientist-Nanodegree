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
    ## delete rows that contains related-2
    ##related_2_index = categories[categories['categories'].str.contains("related-2")].index
    ##categories = categories.drop(categories.index[related_2_index])
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
       # expand the categories column
    categories = df.categories.str.split(';', expand=True)
    row = categories[:1]

    # get the category names
    category_colnames = row.applymap(lambda s: s[:-2]).iloc[0, :].tolist()
    categories.columns = category_colnames

    # get only the last value in each value as an integer
    categories = categories.applymap(lambda s: int(s[-1]))

    # add the categories back to the original df
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)

    # clean up the final data
    df.drop_duplicates(subset='message', inplace=True)
    df.dropna(subset=category_colnames, inplace=True)
    df.related.replace(2, 0, inplace=True)
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
    engine = create_engine('sqlite:///' + database_filename )
    df.to_sql('DisasterResponse', engine, index=False, if_exists='replace')


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