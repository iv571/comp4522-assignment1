#Reads the .csv file

#Navigates through the list of transactions

#A simulation of a random failure is executed:

#it could return failure or success

#If a failure did occur, it calls the program to perform roll-back

import sys
assert sys.version_info >= (3, 5)
import pandas as pd



# Read the CSV file into a DataFrame

df = pd.read_csv("Employees_DB_ADV.csv")



# List of transactions

transactions = [['1', 'Department', 'Music'],

                ['5', 'Civil_Status', 'Divorced'],

                ['15', 'Salary', 200000]]  # Changed '200000' to 200000 (int)



def search_transactions(transactions, DB_Log):

    '''

    Search through the first set of values in transactions

    and find matching rows in DB_Log.

    '''

    matching_rows = []

    for transaction in transactions:

        transaction_id = int(transaction[0])  # Convert transaction ID to int

        matching_row = DB_Log[DB_Log.index == transaction_id-1]

        mathcing_row_index= DB_Log.index == transaction_id-1

        if not matching_row.empty:


            possibilities = ['First_name'], ['Last_name'], ['Salary'], ['Department'], ['Civil_Status']

            #DB_Log[DB_Log.index == transaction_id-1] = matching_row

            matching_rows.append(matching_row)

    #         for possible in possibilities:

    #             if transaction[1] == possible:

    #                 # DB_Log[] = matching_row_index

    # print(DB_Log)

    return matching_rows


def main():

    # Print initial DataFrame

    print("Initial DB_Log:")

    print(df.head(15))  # Display the first 15 rows

    

    # Search through transactions

    matching_rows = search_transactions(transactions, df)

    print(DB_Log.index)

    # Print matching rows

    print("\nMatching Rows:")

    for row in matching_rows:

        print(row)










def main():

  

    number_of_transactions = len(transactions)

    must_recover = False

    data_base = pd.read_file('Employees_DB_ADV.csv')

    DB_Log = [] #initialize database log to track transactions

    failure = is_there_a_failure()

    failing_transaction_index = None

    while not failure:

        # Process transaction

        for index in range(number_of_transactions):

            print(f"\nProcessing transaction No. {index+1}.")  

            #<--- Your CODE goes here (to process transaction at hand)

            print("UPDATES have not been committed yet...\n")

            failure = is_there_a_failure()

            if failure:

                must_recover = True

                failing_transaction_index = index + 1

                print('There was a failure whilst processing transaction \  No. {failing_transaction_index}.')

                break

            else:

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

    for item in data_base:

        print(item)



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