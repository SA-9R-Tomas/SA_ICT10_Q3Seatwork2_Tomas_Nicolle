# Seatworkk 2 - Second Quarter
from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    # Check if registration is selected
    reg_element = document.querySelector('input[name="registration"]:checked')
    if not reg_element:
        display('Please select whether you completed online registration.', target='output')
        return
    registration = reg_element.value
    
    # Check if clearance is selected
    clear_element = document.querySelector('input[name="clearance"]:checked')
    if not clear_element:
        display('Please select whether you have medical clearance.', target='output')
        return
    clearance = clear_element.value
    
    # Check if commitment is selected
    commitment_element = document.querySelector('input[name="commitment"]:checked')
    if not commitment_element:
        display('Please select whether you can commit to attending games/practices.', target='output')
        return
    commitment = commitment_element.value
    
    # Check if unsportsmanlike behavior acknowledgment is selected
    unsports_element = document.querySelector('input[name="unsportsmanlike"]:checked')
    if not unsports_element:
        display('Please acknowledge the unsportsmanlike behavior disqualification policy.', target='output')
        return
    unsportsmanlike = unsports_element.value
    
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display(f'Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')
    elif commitment != 'committed':
        display(f'Not eligible: commitment to attend games/practices is required.', target='output')
    elif unsportsmanlike != 'understood':
        display(f'Not eligible: you must acknowledge the unsportsmanlike behavior disqualification policy.', target='output')
    elif section == 'emerald':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = '<img src="blue bears.jpg" style="max-width: 300px;">'
    elif section == 'ruby':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = '<img src="red bulldogs.jpg" style="max-width: 300px;">'
    elif section == 'sapphire':
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = '<img src="green hornets.jpg" style="max-width: 300px;">'
    else: 
        display(f'Congratulations! You are part of the ...', target='output')
        document.getElementById("image").innerHTML = '<img src="yellow tigers.jpg" style="max-width: 300px;">'