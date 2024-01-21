import pygame
import random
# import time


class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        val=self.items.pop()
        return val

    def isOverflown(self):
        return len(self.items) >= 5
    
    def isUnderflown(self):
        return len(self.items) <= 0
    
    def peek(self):
        return self.items[-1], len(self.items)
    
    
class StackVisual():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 450))
        self.clock = pygame.time.Clock()
        self.stack=Stack()
        self.stackObjects = []
        self.font=pygame.font.SysFont("comicsansms", 20)
        
        self.stackReq()
        
        self.displayMsg(msg="Press Space to push", pos=(420, 100), color=(255,255,255,128))
        self.displayMsg(msg="Backspace to pop", pos=(420, 130), color=(255,255,255,128))
        self.displayMsg(msg="Esc to reset", pos=(420, 160), color=(255,255,255,128))
        
    
    def stackReq(self):
        font = pygame.font.SysFont("comicsansms", 36)
        stext = font.render("Stack", True, (255, 255, 255))
        stextRect = stext.get_rect()
        stextRect.center = (320, 30)
        self.screen.blit(stext, stextRect)
        
        self.blockSize = (100, 50)
        self.stackBlockPosition=(130, 240-self.blockSize[1]*2)
        self.stackBlock = pygame.Surface((self.blockSize[0],self.blockSize[1]*5), pygame.SRCALPHA)
        self.stackBlock.fill((200,200,200,128))
        pygame.draw.rect(self.stackBlock, (0, 100, 255), pygame.Rect(0,0, 100, 300), 3)
        
    def buttons(self, placeHolder, coordinates):
        font=pygame.font.SysFont("comicsansms", 20)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(coordinates))
        text=font.render(placeHolder, True, (10, 10, 10))
        textRect = text.get_rect()
        textRect.center = (coordinates[0]+coordinates[2]/2, coordinates[1]+coordinates[3]/2)
        self.screen.blit(text, textRect)
        
    def run(self):
        done=False
        self.msgDisplay = False
        
        self.buttons("Push", (320, 200, 100, 50))
        self.buttons("Pop", (450, 200, 100, 50))
        self.buttons("Reset", (380, 280, 100, 50))
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.displayPush()
                    if event.key==pygame.K_BACKSPACE:
                        self.displayPop()
                    
                    if event.key==pygame.K_ESCAPE:
                        self.stack = Stack()
                        self.stackObjects = []
                        self.screen.fill((0, 0,0), (80, 80, 200, 50))
                        self.msgDisplay = False               
                        
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if 320<=event.pos[0]<=420 and 200<=event.pos[1]<=250:
                            self.displayPush()
                                
                        if 450<=event.pos[0]<=550 and 200<=event.pos[1]<=250:
                            self.displayPop()
                    
                        if 380<=event.pos[0]<=480 and 280<=event.pos[1]<=330:
                            self.stack = Stack()
                            self.stackObjects = []
                            self.screen.fill((0, 0,0), (80, 80, 200, 50))               
                        
            self.displayStack()
            self.screen.blit(self.stackBlock,  self.stackBlockPosition)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
                        
    def displayStack(self):
        self.screen.fill((0, 0,0), (self.stackBlockPosition[0]-70, self.stackBlockPosition[1]-self.blockSize[1], 50, self.blockSize[1]*5+self.blockSize[1]))
        
        size = len(self.stackObjects)
        for i in range(size):
            self.stackObjects[i].fill((250,250,250,128))
            pygame.draw.rect(self.stackObjects[i], (0, 30, 30), pygame.Rect(0,0, self.blockSize[0], self.blockSize[1]), 3)
            
            text=self.font.render(str(self.stack.items[i]), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (50, 25)
            self.stackObjects[i].blit(text, textRect)
            
            self.screen.blit(self.stackObjects[i], (self.stackBlockPosition[0], 340-self.blockSize[1]*i))
            
            if i==size-1:
                topText = self.font.render("Top", True, (255, 255, 255, 128))
                topTextRect = topText.get_rect() 
                topTextRect.center = (self.stackBlockPosition[0]-50, 340-self.blockSize[1]*i+15)
                self.screen.blit(topText, topTextRect)
                
    def displayMsg(self,msg, color=(255, 255, 255), pos=(180, 100)):
        text=self.font.render(msg, True, color)
        textRect = text.get_rect()
        textRect.center = pos
        self.screen.blit(text, textRect)
        
    def displayPush(self):
        if self.stack.isOverflown():
            self.displayMsg(msg="Stack is full")
            self.msgDisplay = True
        else:
            self.stack.push(random.randint(0, 100))
            self.stackObjects.append(pygame.Surface(self.blockSize, pygame.SRCALPHA)) 
            if self.msgDisplay:
                self.msgDisplay = False
                self.screen.fill((0, 0,0), (80, 80, 200, 50))
                
    def displayPop(self):
        if  self.stack.isUnderflown():
            self.displayMsg(msg="Stack is empty")
            self.msgDisplay = True
        else:
            self.stack.pop()
            self.stackObjects.pop()
            if self.msgDisplay:
                self.msgDisplay = False
                self.screen.fill((0, 0,0), (80, 80, 200, 50))               

if __name__ == '__main__':
    StackVisual().run()
    