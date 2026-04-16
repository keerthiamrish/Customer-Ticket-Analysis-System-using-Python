
#Step 1: Preloaded Tickets
#Begin your program with the following dictionary of lists containing 10 customer tickets:
ticket_data={
    'Ticket_No':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Customer_Name':[ 'Ravi', 'Meera', 'Sam', 'Anu', 'Rakesh', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Issue_Description': [' Internet not working!!! ', 'slow response, very poor service ',
    'GREAT support! issue resolved.',' okay... need help ', 'not BAD but slow', 'Excellent guidance', 'Very Helpful',
    'good support and good behaviour!', 'Poor handling of technical issue', 'Satisfied. Could be better.','Good service... quick response.'],
    'Priority': ['High', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'High', 'Low', 'Medium']
}
ticket_data
# Print the initial ticket data in a readable format
for i in range(len(ticket_data['Ticket_No'])):
 print("************TICKET DETAILS*************")
 print(f"Ticket_No:          {ticket_data['Ticket_No'][i]}")
 print(f"Customer_Name:      {ticket_data['Customer_Name'][i]}")
 print(f"Issue_Description:  {ticket_data['Issue_Description'][i]}")
 print(f"Priority:           {ticket_data['Priority'][i]}")
 print()

count = int(input("How many new tickets do you want to add? "))
Ticket_No = len(ticket_data['Ticket_No']) +1
for i in range(count):
 print("\n--- Enter Ticket Details ---")
 name = input("Enter the customer name:")
 issue = input("Enter the Issue Description:")
 priority = input("Enter the Priority High/Medium/Low:")
ticket_data['Ticket_No'].append(Ticket_No)
ticket_data['Customer_Name'].append(name)
ticket_data['Issue_Description'].append(issue)
ticket_data['Priority'].append(priority)
print(f"Ticket {Ticket_No} Added Successfully")

#Remove the punctuation marks from the issue description.
import re
ticket_data['Issue_Description'] = [re.sub(r'[.,!?-]', '', desc) for desc in ticket_data['Issue_Description']]

# Print the initial ticket data in a readable format
for i in range(len(ticket_data['Ticket_No'])):
 print("************TICKET DETAILS*************")
 print(f"Ticket_No:          {ticket_data['Ticket_No'][i]}")
 print(f"Customer_Name:      {ticket_data['Customer_Name'][i]}")
 print(f"Issue_Description:  {ticket_data['Issue_Description'][i]}")
 print(f"Priority:           {ticket_data['Priority'][i]}")

ticket_data['Issue_Description'] = [desc.lower() for desc in ticket_data['Issue_Description']]
ticket_data
# Print the initial ticket data in a readable format
for i in range(len(ticket_data['Ticket_No'])):
 print("************TICKET DETAILS*************")
 print(f"Ticket_No:          {ticket_data['Ticket_No'][i]}")
 print(f"Customer_Name:      {ticket_data['Customer_Name'][i]}")
 print(f"Issue_Description:  {ticket_data['Issue_Description'][i]}")
 print(f"Priority:           {ticket_data['Priority'][i]}")

ticket_data['Issue_Description'] = [desc.lstrip() for desc in ticket_data['Issue_Description']]
ticket_data
# Print the initial ticket data in a readable format
for i in range(len(ticket_data['Ticket_No'])):
 print("************TICKET DETAILS*************")
 print(f"Ticket_No:          {ticket_data['Ticket_No'][i]}")
 print(f"Customer_Name:      {ticket_data['Customer_Name'][i]}")
 print(f"Issue_Description:  {ticket_data['Issue_Description'][i]}")
 print(f"Priority:           {ticket_data['Priority'][i]}")
 print()

ticket_data['Issue_Description'] = [desc.replace('okay', 'ok') for desc in ticket_data['Issue_Description']]
ticket_data
# Print the initial ticket data in a readable format
for i in range(len(ticket_data['Ticket_No'])):
 print("************TICKET DETAILS*************")
 print(f"Ticket_No:          {ticket_data['Ticket_No'][i]}")
 print(f"Customer_Name:      {ticket_data['Customer_Name'][i]}")
 print(f"Issue_Description:  {ticket_data['Issue_Description'][i]}")
 print(f"Priority:           {ticket_data['Priority'][i]}")
 print()

def count_tickets_with_word(word):
    # Convert search word to lowercase
    word = word.lower()

    # Count rows where description contains the word
    count = 0
    for description in ticket_data['Issue_Description']:
        if word in description.lower():
            count += 1

    return count
print("Ticket contains the word Poor:",count_tickets_with_word('poor'))
print("Ticket contains the word Good:",count_tickets_with_word('good'))
print("Ticket contains the word Slow:",count_tickets_with_word('slow'))
print("Ticket contains the word Internet:",count_tickets_with_word('internet'))

high_count = ticket_data['Priority'].count('High')
medium_count = ticket_data['Priority'].count('Medium')
low_count = ticket_data['Priority'].count('Low')

print("High Priority Tickets  :", high_count)
print("Medium Priority Tickets:", medium_count)
print("Low Priority Tickets   :", low_count)

# Initialize variables
max_word_count = 0
max_index = 0

# Loop through all issue descriptions
for i in range(len(ticket_data['Issue_Description'])):

    description = ticket_data['Issue_Description'][i]
    word_count = len(description.split())

    if word_count > max_word_count:
        max_word_count = word_count
        max_index = i
print("\n========== TICKET WITH LONGEST ISSUE ==========\n")

print("Ticket Number :", ticket_data['Ticket_No'][max_index])
print("Customer Name :", ticket_data['Customer_Name'][max_index])
print("Issue Text    :", ticket_data['Issue_Description'][max_index])
print("Word Count    :", max_word_count)

all_text = " ".join(ticket_data['Issue_Description'])
words = all_text.split()
unique_words = set(words)
sorted_words = sorted(unique_words)
print("\n========== UNIQUE WORD ANALYSIS ==========\n")

print("Total Unique Words:", len(unique_words))
print("\nSorted Unique Words List:")
print(sorted_words)