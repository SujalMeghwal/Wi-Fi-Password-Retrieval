import subprocess

# Function to retrieve Wi-Fi passwords
def retrieve_wifi_passwords():
    command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [line.split(':')[1].strip() for line in command_output if "All User Profile" in line]

    for profile in profiles:
        try:
            password_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode(
                'utf-8').split('\n')
            password_lines = [line.split(':')[1].strip() for line in password_output if "Key Content" in line]

            if len(password_lines) > 0:
                print(f'Wi-Fi Profile: {profile}')
                print(f'Password: {password_lines[0]}')
                print('-' * 30)
        except subprocess.CalledProcessError:
            print(f'Error retrieving password for profile: {profile}')
            print('-' * 30)

# Main function
def main():
    retrieve_wifi_passwords()
    input('Press enter to close the program...')  # Wait for user input

# Execute the main function
if __name__ == '__main__':
    main()
