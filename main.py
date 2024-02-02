#Reads the .csv file
#Navigates through the list of transactions
#A simulation of a random failure is executed:
#it could return failure or success
#If a failure did occur, it calls the program to perform roll-back

def main():
    number_of_transactions = len(transactions)
    must_recover = False
    data_base = read_file('Employees_DB_ADV.csv')
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
                print(f'There was a failure whilst processing transaction \
                No. {failing_transaction_index}.')
                break
            else:
                print(f'Transaction No. {index+1} has been commited! 
                Changes are permanent.')
                
    if must_recover:
        #Call your recovery script
        recovery_script(DB_Log) 
        ### Call the recovery function to restore DB to sound state
    else:
        # All transactiones ended up well
        print("All transaction ended up well.")
        print("Updates to the database were committed!\n")

    print('The data entries AFTER updates -and RECOVERY, if necessary-
    are presented below:')
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

def transaction_processing(): #<-- Your CODE
    '''
    1. Process transaction in the transaction queue.
    2. Updates DB_Log accordingly
    3. This function does NOT commit the updates, just execute them
    '''
    pass
