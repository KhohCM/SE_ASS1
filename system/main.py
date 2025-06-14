import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import pygame
from tkinter import *
from tkvideo import tkvideo

class RockPaperScissorsGame:
    def __init__(self):
        pygame.mixer.init()
        self.load_sounds()

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.detector = HandDetector(maxHands=1)

        self.timer = 0
        self.stateResult = False
        self.startGame = False
        self.scores = [0, 0]
        self.randomNumber = 1
        self.winnerText = ""
        self.gameMode = None
        self.roundNumber = 1
        self.tournamentWinnerText = ""
        self.tournamentEndTime = None
        self.videoToPlay = None

        self.buttons = {
            "easy": (50, 660, 200, 710),
            "medium": (250, 660, 400, 710),
            "hard": (450, 660, 600, 710),
        }

        cv2.namedWindow("BG", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("BG", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback("BG", self.mouse_click)
    
    def play_cutscene(self):
        cutscene_images = [
            "Resources/s1.png", "Resources/s3.png", "Resources/s2.png",
            "Resources/s4.png", "Resources/s5.png", "Resources/s6.png"
        ]
        screen_width = 1920  # Or use your monitor's actual width
        screen_height = 1080  # Or use your monitor's actual height

        cv2.namedWindow("Cutscene", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Cutscene", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        index = 0
        while index < len(cutscene_images):
            img = cv2.imread(cutscene_images[index])
            if img is None:
                print(f"Could not load {cutscene_images[index]}")
                index += 1
                continue

            img_resized = cv2.resize(img, (screen_width, screen_height))
            cv2.imshow("Cutscene", img_resized)

            key = cv2.waitKey(0)
            if key == ord('s'):
                index += 1
            elif key == ord('q'):
                cv2.destroyAllWindows()
                exit()

        cv2.destroyWindow("Cutscene")


    def load_sounds(self):
        self.sound_player_win = pygame.mixer.Sound("Resources/player_win.mp3")
        self.sound_ai_win = pygame.mixer.Sound("Resources/ai_win.mp3")
        self.sound_tournament_end = pygame.mixer.Sound("Resources/tournament_end.mp3")
        self.sound_select_mode = pygame.mixer.Sound("Resources/select_mode.mp3")
        self.sound_draw = pygame.mixer.Sound("Resources/draw.mp3")
    
    
    


    def get_ai_move(self, player_move=None):
        if self.gameMode == "easy":
            predefined_moves = [3, 1, 2, 3, 1]
            return predefined_moves[(self.roundNumber - 1) % len(predefined_moves)]
        elif self.gameMode == "medium":
            return random.randint(1, 3)
        elif self.gameMode == "hard":
            if player_move == 1:
                return 2
            elif player_move == 2:
                return 3
            elif player_move == 3:
                return 1
        return random.randint(1, 3)

    def mouse_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            for mode, (x1, y1, x2, y2) in self.buttons.items():
                if x1 <= x <= x2 and y1 <= y <= y2:
                    self.gameMode = mode
                    self.startGame = True
                    self.initialTime = time.time()
                    self.stateResult = False
                    self.winnerText = ""
                    pygame.mixer.Sound.play(self.sound_select_mode)
                    print(f"Selected Mode: {mode.capitalize()}")

    def show_result(self):
        if self.stateResult or self.tournamentWinnerText:
            if self.randomNumber:
                imgAI = cv2.imread(f'Resources/{self.randomNumber}.png', cv2.IMREAD_UNCHANGED)
                if imgAI is not None:
                    self.imgBG = cvzone.overlayPNG(self.imgBG, imgAI, (149, 310))
            if self.tournamentWinnerText:
                cv2.putText(self.imgBG, self.tournamentWinnerText, (250, 350), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 5)
            else:
                cv2.putText(self.imgBG, self.winnerText, (380, 480), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)

    def play_video(self):
        if time.time() - self.tournamentEndTime > 2:
            title_map = {"player": "Congratulations!", "ai": "Game Over", "draw": "It's a Draw!"}
            video_map = {
                "player": "Resources/peaceful.mp4",
                "ai": "Resources/world_end.mp4",
                "draw": "Resources/draw.mp4"
            }
            if self.videoToPlay:
                w = Tk()
                w.title(title_map[self.videoToPlay])

                # Fullscreen setup
                screen_width = w.winfo_screenwidth()
                screen_height = w.winfo_screenheight()
                w.geometry(f"{screen_width}x{screen_height}")
                w.attributes('-fullscreen', True)

                lblVideo = Label(w)
                lblVideo.pack(fill="both", expand=True)

                player = tkvideo(video_map[self.videoToPlay], lblVideo, loop=0, size=(screen_width, screen_height))
                player.play()

                # Bind Escape and 'q' key to close the window
                def exit_fullscreen(event):
                    w.destroy()
                w.bind("<Escape>", exit_fullscreen)
                w.bind("q", exit_fullscreen)
                w.bind("Q", exit_fullscreen)

                w.mainloop()

                self.tournamentEndTime = None
                self.videoToPlay = None
                self.tournamentWinnerText = ""



    def run(self):
        while True:
            self.imgBG = cv2.imread("Resources/BG.png")
            success, img = self.cap.read()
            imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
            imgScaled = imgScaled[:, 80:480]

            hands, img = self.detector.findHands(imgScaled)

            if self.startGame:
                self.tournamentWinnerText = ""
                if not self.stateResult:
                    self.timer = time.time() - self.initialTime
                    cv2.putText(self.imgBG, str(int(self.timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

                    if self.timer > 3:
                        self.stateResult = True
                        self.timer = 0
                        playerMove = None

                        if self.gameMode == "hard" and hands and len(hands) > 0:
                            try:
                                fingers = self.detector.fingersUp(hands[0])
                                if fingers == [0, 0, 0, 0, 0]:
                                    playerMove = 1
                                elif fingers == [1, 1, 1, 1, 1]:
                                    playerMove = 2
                                elif fingers == [0, 1, 1, 0, 0]:
                                    playerMove = 3
                            except Exception as e:
                                print("Hand detection error:", e)

                        self.randomNumber = self.get_ai_move(playerMove)

                if self.stateResult:
                    playerMove = None
                    if hands and len(hands) > 0:
                        try:
                            fingers = self.detector.fingersUp(hands[0])
                            if fingers == [0, 0, 0, 0, 0]:
                                playerMove = 1
                            elif fingers == [1, 1, 1, 1, 1]:
                                playerMove = 2
                            elif fingers == [0, 1, 1, 0, 0]:
                                playerMove = 3
                        except Exception as e:
                            print("Hand detection error:", e)

                    if playerMove is None:
                        self.scores[0] += 1
                        self.winnerText = "No move! AI wins this round"
                        self.sound_ai_win.play()
                    else:
                        if (playerMove == 1 and self.randomNumber == 3) or \
                           (playerMove == 2 and self.randomNumber == 1) or \
                           (playerMove == 3 and self.randomNumber == 2):
                            self.scores[1] += 1
                            self.winnerText = "Player wins this round"
                            self.sound_player_win.play()
                        elif (playerMove == 3 and self.randomNumber == 1) or \
                             (playerMove == 1 and self.randomNumber == 2) or \
                             (playerMove == 2 and self.randomNumber == 3):
                            self.scores[0] += 1
                            self.winnerText = "AI wins this round"
                            self.sound_ai_win.play()
                        else:
                            self.winnerText = "It's a draw"
                            self.sound_draw.play()

                    self.roundNumber += 1
                    self.startGame = False

                    if self.roundNumber > 5:
                        if self.scores[1] > self.scores[0]:
                            self.tournamentWinnerText = "Player wins the tournament!"
                            self.videoToPlay = "player"
                        elif self.scores[0] > self.scores[1]:
                            self.tournamentWinnerText = "AI wins the tournament!"
                            self.videoToPlay = "ai"
                        else:
                            self.tournamentWinnerText = "The tournament is a draw!"
                            self.videoToPlay = "draw"
                        self.tournamentEndTime = time.time()
                        self.sound_tournament_end.play()
                        self.roundNumber = 1
                        self.scores = [0, 0]

            for mode, (x1, y1, x2, y2) in self.buttons.items():
                color = (0, 255, 0) if mode == "easy" else (0, 255, 255) if mode == "medium" else (0, 0, 255)
                thickness = -1 if self.gameMode == mode else 2
                cv2.rectangle(self.imgBG, (x1, y1), (x2, y2), color, thickness)
                cv2.putText(self.imgBG, mode.capitalize(), (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

            self.imgBG[232:652, 793:1193] = imgScaled
            self.show_result()

            cv2.putText(self.imgBG, str(int(self.timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (0, 0, 255), 4)
            cv2.putText(self.imgBG, str(self.scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
            cv2.putText(self.imgBG, str(self.scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
            cv2.putText(self.imgBG, f"Round {self.roundNumber}", (540, 190), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)



            if self.tournamentEndTime is not None:
                self.play_video()

            cv2.imshow("BG", self.imgBG)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_cutscene()  
    game.run()