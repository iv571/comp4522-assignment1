"""
COMP-4522 Assignment 1
Authors: Aldo Ortiz, Iyan Velji
Date: February 16, 2024

1. Reads CSV file
2. Navigates through the list of transactions
3. A simulation of a random failure is executed
4. If a failure did occur, it calls the program to perform roll-back

"""

import sys
assert sys.version_info >= (3, 5)
import pandas as pd
import random


# Read the CSV file into a DataFrame and backup DataFrame
df = pd.read_csv("Employees_DB_ADV.csv")
df2 = pd.read_csv("Employees_DB_ADV.csv")


def search_transactions(transactions, df):

    '''
    Search through the first set of values in transactions

    and find matching rows in DB_Log.

    '''

    matching_rows = []

    for transaction in transactions:

        transaction_id = int(transaction[0])  # Convert transaction ID to int

        matching_row = df[df.index == transaction_id-1]

        matching_row_index= df.index == transaction_id-1

        if not matching_row.empty:

            matching_rows.append(matching_row)

    return matching_rows


def main():
    
    # List of transactions
    transactions = [['1', 'Department', 'Music'],
                    ['5', 'Civil_status', 'Divorced'],
                    ['15', 'Salary', 600000],
                    ['4', 'Last_name', "Joe"]] 
    #initialize database log to track transactions
    DB_Log = [] 
    print("Starting transactions ...")


    number_of_transactions = len(transactions)

    must_recover = False

    failure = is_there_a_failure()

    failing_transaction_index = None

    while not failure:

        # Process transaction
        x = 0

        for index in range(number_of_transactions):

            print(f"\nProcessing transaction No. {index+1}.")  

            df.at[int(transactions[x][0])-1, transactions[x][1]]  =  transactions[x][2]
            
            print("Value Changed to:")
            print(df.at[int(transactions[x][0])-1, transactions[x][1]])

            print("Updated DB:")
            print(df.head(16))

            print("UPDATES have not been committed yet...\n")

            x += 1

            failure = is_there_a_failure()

            if failure:

                must_recover = True
                recovery_script(df)

                failing_transaction_index = index + 1

                print(f'There was a failure whilst processing transaction \  No. {failing_transaction_index}.')

                break

            else:
                #Commit Changes
                df2 = df.copy()
                print(f"\nTransaction No. {index+1} has been commited! Changes are permanent.")

           

    if must_recover:

        #Call your recovery script

        recovery_script(DB_Log) 

        ### Call the recovery function to restore DB to sound state

    else:

        # All transactiones ended up well

        print("All transaction ended up well.")

        print("Updates to the database were committed!\n")



    print('The data entries AFTER updates -and RECOVERY, if necessary-are presented below:')

  
def is_there_a_failure()->bool:

    '''

    Simulates randomly a failure, returning True or False, accordingly

    '''

    value = random.randint(0,1)

    if value == 1:

        result = True

    else:

        result = False

    return result


def recovery_script(log:list):  #<--- Your CODE

    '''

    Restore the database to stable and sound condition, by processing

    the DB log.

    '''

    print("Calling your recovery script with DB_Log as an argument.")

    print("Recovery in process ...\n")

    print("entered recovery")

    df2.to_csv("Employees_DB_output.csv", index=False)

    print(df2.head(16))

    print("Changes have been rolled back to the last committed transaction")

    pass

def transaction_processing(transactions, DB_Log): #<-- Your CODE

    '''

    1. Process transaction in the transaction queue.

    2. Updates DB_Log accordingly

    3. This function does NOT commit the updates, just execute them

    '''

    for transaction in transactions:

        # Extract transaction details

        transaction_id, column_name, new_value = transaction

        

        # Find the corresponding entry in the DB log

        for entry in DB_Log:

            if entry[0] == transaction_id:

                # Update the value in the DB log

                entry[2] = new_value

                break

        else:

            # If transaction ID not found, add a new entry to the DB log

            DB_Log.append([transaction_id, column_name, new_value])

    pass


main()