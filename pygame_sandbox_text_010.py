welcome_msg = "pygame_sandbox_test.py open"
print (welcome_msg)



def nip_front_line_from(whole_string, goal_wrap):
    wrap = goal_wrap
    print("wrap = " + str(wrap))
    if(wrap >= len(whole_string)):
        print("wrap longer than whole_string")
        wrap = len(whole_string) - 1
        nipped_string = whole_string
        nipped_line = ''
    else:
        while(whole_string[wrap].isspace() != True):
            wrap -= 1   
    
        nipped_string = whole_string[:wrap]
        nipped_line = whole_string[wrap+1:]
    return nipped_string, nipped_line


def wrap_string(raw_str, max_wrap):
    print("original format: " + raw_str)
    new_text = []
    current_raw = raw_str
    while (len(current_raw) >= 1):
        next_line, new_raw = nip_front_line_from(current_raw, max_wrap)
        new_text.append(next_line)
        current_raw = new_raw
    return new_text


def read_list(list_in_question):
    for item in list_in_question:
        print(item)


#def wrap_dialogue(dialogue, wrap):
#    a = wrap_string(dialogue, wrap)
    




other_raw_test_text = "The night is lovely dark and deep but I have promises to keep"\
                      "and miles to go before I sleep and miles to go before I sleep"
raw_test_text = "Peter Piper picked a peck of pickled peppers"
new_test_text = wrap_string(other_raw_test_text, 20)
read_list(new_test_text)




