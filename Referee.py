def get_hole_pos():
    choices = ['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15']
    print("here is the board!\n"

          "               1 \n"
          "               o \n"
          "             2/ \\3 \n"
          "             o — o \n"
          "           4/ \\5/ \\6 \n"
          "           o — o — o \n"
          "         7/ \\8/ \\9/ \\10 \n"
          "         o — o — o — o \n"
          "       11/\\12/\\13/\\14/\\15 \n"
          "       o — o — o — o — o ")
    user_choice = input("Enter a hole to leave empty.").lower()

    while user_choice not in choices:
        user_choice = input("Invalid choice.").lower()
    return user_choice
    print(user_choice," Is the position sected to have an empty hole.")

def printing_board():
    print("here is the starting board!\n"
    
                  "              1 \n"
                 f"             {} \n"
                "             2/ \\3 \n"
               f"            {} — {} \n"
              "           4/ \\5/ \\6 \n"
             f"           {} — {} — {} \n"
            "         7/ \\8/ \\9/ \\10 \n"
           f"         {} — {} — {} — {} \n"
         "       11/\\12/\\13/\\14/\\15 \n"
         f"       {} — {} — {} — {} — {} ")

