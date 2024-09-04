def get_hole_pos():
    choices = ['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15']
    user_choice = input("Enter a hole to leave empty.").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice.").lower()
    return user_choice


