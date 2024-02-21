board=["_","_","_",
       "_","_","_",
       "_","_","_" ]

def print_board():
              print(board[0] + " | " + board[1] + " | " + board[2] )
              print(board[3] + " | " + board[4] + " | " + board[5] )
              print(board[6] + " | " + board[7] + " | " + board[8] )

def play_game():
              print_board()
              current_player="X"
              game_over=False
              while not game_over:
                            take_turn(current_player)
                            game_result=check_game_over()
                            if game_result=="Wins":
                                          print(current_player+"'s wins")
                                          game_over=True
                            elif game_result=="Tie":
                                          print("Its is a Tie")
                                          game_over=True
                            else:
                                          if current_player=="X":
                                                        current_player="O"
                                          else:
                                                        current_player="X"
def take_turn(player):
               print(player+ "'s turn")
               position=input("choose a number from 1-9 : ")
               numbers=["1","2","3","4","5","6","7","8","9"]
               while position not in numbers:
                             position=input("InValid Input.. Choose a Valid  number from 1-9 : ")
               position=int(position)-1
               while board[position]!="_":
                            position=int(input("position already taken .Choose a different position : "))-1
                           
               board[position]=player
               print_board()

def check_game_over():
              if "_" not in board:
                            return "Tie"
              
              
              elif( (board[0]==board[1]==board[2]!="_") or
                   (board[3]==board[4]==board[5]!="_") or
                   (board[6]==board[7]==board[8]!="_") or
                   (board[0]==board[3]==board[6]!="_") or
                   (board[1]==board[4]==board[7]!="_") or
                   (board[2]==board[5]==board[8]!="_") or
                   (board[0]==board[4]==board[8]!="_") or
                   (board[2]==board[4]==board[6]!="_") ):
                            return "Wins"
    
              else:
                            return "play"

play_game()
               
 
             
             
