import pygame

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.square_size = 80
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.valid_moves = []
        self.turn = 'w'  # 'w' for White, 'b' for Black
        self.flipped = False
        self.setup_board()

    def setup_board(self):
        self.board[1] = ['b_pawn'] * 8
        self.board[6] = ['w_pawn'] * 8

        self.board[0][0] = self.board[0][7] = 'b_rook'
        self.board[7][0] = self.board[7][7] = 'w_rook'

        self.board[0][1] = self.board[0][6] = 'b_knight'
        self.board[7][1] = self.board[7][6] = 'w_knight'

        self.board[0][2] = self.board[0][5] = 'b_bishop'
        self.board[7][2] = self.board[7][5] = 'w_bishop'

        self.board[0][3] = 'b_queen'
        self.board[7][3] = 'w_queen'

        self.board[0][4] = 'b_king'
        self.board[7][4] = 'w_king'

    def draw(self, screen, images):
        light_color = (240, 217, 181)
        dark_color = (181, 136, 99)

        for row in range(self.rows):
            for col in range(self.cols):
                draw_row = 7 - row if self.flipped else row
                draw_col = 7 - col if self.flipped else col

                color = light_color if (draw_row + draw_col) % 2 == 0 else dark_color
                pygame.draw.rect(
                    screen, color,
                    pygame.Rect(draw_col * self.square_size, draw_row * self.square_size,
                                self.square_size, self.square_size)
                )

                if self.selected_piece == (row, col):
                    pygame.draw.rect(
                        screen, (255, 0, 0),
                        pygame.Rect(draw_col * self.square_size, draw_row * self.square_size,
                                    self.square_size, self.square_size), 3
                    )

                if (row, col) in self.valid_moves:
                    pygame.draw.circle(
                        screen, (0, 255, 0),
                        (draw_col * self.square_size + self.square_size // 2,
                         draw_row * self.square_size + self.square_size // 2), 10
                    )

                piece = self.board[row][col]
                if piece:
                    screen.blit(images[piece], (draw_col * self.square_size, draw_row * self.square_size))

        font = pygame.font.SysFont("arial", 24)
        if self.king_in_check('w'):
            text = font.render("White is in Check!", True, (255, 0, 0))
            screen.blit(text, (10, 10))
        elif self.king_in_check('b'):
            text = font.render("Black is in Check!", True, (255, 0, 0))
            screen.blit(text, (10, 10))

        if self.checkmate('w'):
            text = font.render("Checkmate! Black wins.", True, (0, 0, 0))
            screen.blit(text, (180, 10))
        elif self.checkmate('b'):
            text = font.render("Checkmate! White wins.", True, (0, 0, 0))
            screen.blit(text, (180, 10))

    def get_square_under_mouse(self, pos):
        x, y = pos
        col = x // self.square_size
        row = y // self.square_size
        if self.flipped:
            col = 7 - col
            row = 7 - row
        return row, col

    def get_valid_moves(self, row, col):
        piece = self.board[row][col]
        moves = []
        if piece is None:
            return moves

        color, p_type = piece.split("_")
        direction = -1 if color == 'w' else 1

        if p_type == "pawn":
            if 0 <= row + direction < 8 and self.board[row + direction][col] is None:
                moves.append((row + direction, col))
                if (row == 6 and color == 'w') or (row == 1 and color == 'b'):
                    if self.board[row + 2 * direction][col] is None:
                        moves.append((row + 2 * direction, col))
            for dc in [-1, 1]:
                new_row, new_col = row + direction, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = self.board[new_row][new_col]
                    if target and target.startswith(('w_' if color == 'b' else 'b_')):
                        moves.append((new_row, new_col))

        elif p_type == "rook":
            moves += self.linear_moves(row, col, [(-1, 0), (1, 0), (0, -1), (0, 1)], color)

        elif p_type == "bishop":
            moves += self.linear_moves(row, col, [(-1, -1), (-1, 1), (1, -1), (1, 1)], color)

        elif p_type == "queen":
            moves += self.linear_moves(row, col, [(-1, 0), (1, 0), (0, -1), (0, 1),
                                                  (-1, -1), (-1, 1), (1, -1), (1, 1)], color)

        elif p_type == "king":
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = self.board[r][c]
                    if target is None or target.startswith(('w_' if color == 'b' else 'b_')):
                        moves.append((r, c))

        elif p_type == "knight":
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                           (1, -2), (1, 2), (2, -1), (2, 1)]:
                r, c = row + dr, col + dc
                if 0 <= r < 8 and 0 <= c < 8:
                    target = self.board[r][c]
                    if target is None or target.startswith(('w_' if color == 'b' else 'b_')): 
                        moves.append((r, c))
        return moves

    def linear_moves(self, row, col, directions, color):
        moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = self.board[r][c]
                if target is None:
                    moves.append((r, c))
                elif target.startswith(('w_' if color == 'b' else 'b_')):
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves

    def handle_click(self, pos):
        row, col = self.get_square_under_mouse(pos)
        piece = self.board[row][col]

        if self.selected_piece:
            if (row, col) in self.valid_moves:
                from_row, from_col = self.selected_piece
                self.board[row][col] = self.board[from_row][from_col]
                self.board[from_row][from_col] = None
                self.turn = 'b' if self.turn == 'w' else 'w'
                self.flipped = not self.flipped
            self.selected_piece = None
            self.valid_moves = []
        elif piece and piece.startswith(self.turn):
            self.selected_piece = (row, col)
            self.valid_moves = self.get_valid_moves(row, col)
        else:
            self.selected_piece = None
            self.valid_moves = []

    def find_king(self, color):
        target_king = f"{color}_king"
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == target_king:
                    return (row, col)
        return None

    def king_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        opponent_color = 'b' if color == 'w' else 'w'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.startswith(opponent_color):
                    moves = self.get_valid_moves(row, col)
                    if king_pos in moves:
                        return True
        return False

    def checkmate(self, color):
        if not self.king_in_check(color):
            return False
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.startswith(color):
                    moves = self.get_valid_moves(row, col)
                    for move in moves:
                        # Simulate the move
                        original_piece = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = self.board[row][col]
                        self.board[row][col] = None

                        # Check if the king is still in check
                        if not self.king_in_check(color):
                            self.board[row][col] = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = original_piece
                            return False
                        # Revert the move
                        self.board[row][col] = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = original_piece
        return True
