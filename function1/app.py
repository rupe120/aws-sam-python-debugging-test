import global_helper 

def lambda_handler(event, context):
    global_stuff = global_helper.get_global_stuff()
    print(f'App 3 shared helper: {global_stuff}')