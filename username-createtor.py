import random
import argparse

# Generate a list of possible usernames based on the name parts
def generate_username(full_name, include_initial=False):
    # Split the full name into first, middle, and last name (if available)
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = name_parts[-1]
    middle_name = " ".join(name_parts[1:-1]) if len(name_parts) > 2 else ""

    usernames = [
        f"{first_name[0].upper()}{last_name}", # FSmith
        f"{first_name[0].lower()}{last_name}", # fsmith
        f"{first_name[0].upper()}{last_name.lower()}", # Fsmith
        f"{first_name}{last_name[0]}", # FergusS
        f"{first_name.lower()}.{last_name.lower()}", # fergus.smith
        f"{first_name}.{last_name}", # Fergus.Smith
        f"{first_name.lower()},{last_name.lower()}", # fergus,smith
        f"{first_name},{last_name}", # Fergus,smith
        f"{last_name}{first_name[0]}", # SmithF
        f"{first_name[0]}{last_name}", # FSmith
        f"{first_name.lower()}", # fergus
        f"{last_name.lower()}", # smith
        f"{last_name[0].lower()}{first_name.lower()}", # sfergus
        f"{first_name[0].lower()}{last_name.lower()}", # fsmith
        f"{first_name.upper()}{last_name.upper()}", # FSMITH
        f"{last_name.upper()}{first_name.upper()}", # SMITHFERGUS
        f"{full_name.upper()}", # FERGUS SMITH
        f"{first_name}", # Fergus
        f"{last_name}", # Smith
        f"{first_name[0].upper()}.{last_name}", # F.Smith
        f"{first_name}.{last_name[0].upper()}", # FergusS
        f"{first_name[0].upper()}{last_name[0].upper()}", # FS
        f"{first_name.lower()}{last_name.lower()}", # fergussmith
        f"{last_name.lower()}{first_name.lower()}", # smithfergus
        f"{first_name[0].lower()}{last_name[0].lower()}", # fs
    ]

    if middle_name:
        usernames.extend([
            f"{first_name[0].upper()}{middle_name[0].upper()}{last_name}", # FESmith
            f"{first_name[0].upper()}{middle_name[0].upper()}.{last_name}", # FE.Smith
            f"{first_name[0].upper()}.{middle_name[0].upper()}{last_name}", # F.ESmith
            f"{first_name[0].upper()}{middle_name[0].upper()}{last_name[0].upper()}", # FES
            f"{first_name[0].upper()}.{middle_name[0].upper()}{last_name[0].upper()}", # FE.S
            f"{first_name.lower()}{middle_name.lower()}{last_name.lower()}", # fergussmith
            f"{first_name.lower()}.{middle_name.lower()}.{last_name.lower()}", # fergus.smith
            f"{first_name[0].lower()}{middle_name[0].lower()}{last_name.lower()}", # fesmith
            f"{first_name[0].lower()}.{middle_name[0].lower()}{last_name.lower()}", # fe.smith
            f"{first_name[0].upper()}{middle_name.capitalize()}{last_name}", # FergusESmith
            f"{middle_name.lower()}{first_name.lower()}", # esmithfergus
            f"{first_name.capitalize()}{middle_name.capitalize()}", # FergusSmith
            f"{first_name.upper()}{middle_name.upper()}{last_name.upper()}", # FERGUSSMITH
            f"{first_name.lower()}{middle_name.lower()}", # ferguselizabethsmith
            f"{middle_name.lower()}{last_name.lower()}", # elizabethsmith
        ])

    # Include usernames with the first initial and last name
    if include_initial:
        usernames.extend([
            f"{first_name[0]}{last_name}",
            f"{last_name}{first_name[0]}",
        ])

    return usernames

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate a list of possible usernames based on a name.')
    parser.add_argument('-n', '--name', type=str, help='The name to generate usernames for.')
    parser.add_argument('-f', '--file', type=str, help='The name of the file containing the names to generate usernames for.')
    parser.add_argument('-o', '--output', type=str, help='The name of the file to save the usernames to.')
    parser.add_argument('-i', '--include_initial', action='store_true', help='Include usernames with the first initial and last name.')
    args = parser.parse_args()

    # Generate the list of usernames for the specified name or file
    if args.name:
        usernames = generate_username(args.name, args.include_initial)
    elif args.file:
        with open(args.file, 'r') as f:
            names = f.readlines()
        usernames = []
        for name in names:
            name = name.strip()
            if name:
                usernames.extend(generate_username(name, args.include_initial))

    # Output the list of usernames to a file if an output file is specified
    if args.output:
        with open(args.output, 'w') as f:
            for username in usernames:
                f.write(username + '\n')
    else:
        # Print the list of usernames as a word list
        print("\n".join(usernames))
