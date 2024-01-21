import pygame
import random
import time

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        val=self.items.pop(0)
        return val
    
    def isOverflown(self):
        return len(self.items) >= 5
    
    def isUnderflown(self):
        return len(self.items) <= 0
    
    def peek(self):
        return self.items[0], len(self.items)

        

        
class QueueVisual():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 450))
        self.clock = pygame.time.Clock()
        self.queue=Queue()
        self.queueObjects = []
        self.font=pygame.font.SysFont("comicsansms", 20)
        
        self.queueReq()
        
        self.displayMsg(msg="Press Space to add", pos=(180, 300), color=(255,255,255,128))
        self.displayMsg(msg="Backspace to remove", pos=(180, 330), color=(255,255,255,128))
        self.displayMsg(msg="Esc to reset", pos=(180, 360), color=(255,255,255,128))
        
    def queueReq(self):
        font=pygame.font.SysFont("comicsansms", 36)
        qtext = font.render("Queue", True, (255, 255, 255))
        qtextRect = qtext.get_rect()
        qtextRect.center = (320, 30)
        self.screen.blit(qtext, qtextRect)
        
        self.blockSize = (75, 75)
        self.queueBlockPosition=(130, 240-self.blockSize[1]*2)
        self.queueBlock = pygame.Surface((self.blockSize[0]*5,self.blockSize[1]), pygame.SRCALPHA)
        self.queueBlock.fill((200,200,200,128))
        pygame.draw.rect(self.queueBlock, (0, 100, 255), pygame.Rect(0,0, 375, 75), 3)
        
        headText=self.font.render("Head", True, (255, 255, 255))
        headTextRect = headText.get_rect()
        headTextRect.center = (self.queueBlockPosition[0]-50, self.queueBlockPosition[1]+37)
        self.screen.blit(headText, headTextRect)
        
        
    def buttons(self, placeHolder, coordinates):
        font=pygame.font.SysFont("comicsansms", 20)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(coordinates))
        text=font.render(placeHolder, True, (10, 10, 10))
        textRect = text.get_rect()
        textRect.center = (coordinates[0]+coordinates[2]/2, coordinates[1]+coordinates[3]/2)
        self.screen.blit(text, textRect)
        
    def run(self):
        done=False
        self.msgDisplay=False
        
        self.buttons("Enqueue", (400, 250, 100, 50))
        self.buttons("Dequeue", (400, 310, 100, 50))
        self.buttons("Reset", (400, 370, 100, 50))
        
        while not done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done=True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.queue=Queue()
                        self.queueObjects=[]
                        self.screen.fill((0, 0, 0), (200, 210, 200, 30))
                    if event.key==pygame.K_SPACE:
                        self.displayEnqueue()
                    if event.key==pygame.K_BACKSPACE:
                        self.displayDequeue()
                        
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if 400<pos[0]<500 and 250<pos[1]<300:
                        self.displayEnqueue()
                    if 400<pos[0]<500 and 310<pos[1]<360:
                        self.displayDequeue()
                    if 400<pos[0]<500 and 370<pos[1]<420:
                        self.queue=Queue()
                        self.queueObjects=[]
                        self.screen.fill((0, 0, 0), (200, 210, 200, 30))
            self.displayQueue()
            self.screen.blit(self.queueBlock,  self.queueBlockPosition)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
    
    
    def displayQueue(self):
        self.screen.fill((0, 0, 0), (self.queueBlockPosition[0], self.queueBlockPosition[1]+self.blockSize[1]+10, self.blockSize[0]*5, self.blockSize[1]/2))
        
        size=len(self.queue.items)
        for i in range(size):
            self.queueObjects[i].fill((255,255,255))
            pygame.draw.rect(self.queueObjects[i], (0, 0, 0), pygame.Rect(0,0, self.blockSize[0], self.blockSize[1]), 3)
            
            text=self.font.render(str(self.queue.items[i]), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (37, 35)
            self.queueObjects[i].blit(text, textRect)
            self.screen.blit(self.queueObjects[i], (self.queueBlockPosition[0]+i*self.blockSize[0], self.queueBlockPosition[1]))
            
            if i==size-1:
                tailText=self.font.render("Tail", True, (255, 255, 255))
                tailTextRect = tailText.get_rect()
                tailTextRect.center = (self.queueBlockPosition[0]+i*self.blockSize[0]+30, self.queueBlockPosition[1]+self.blockSize[1]+20)
                self.screen.blit(tailText, tailTextRect)
                
                
    
    def displayEnqueue(self):
        if self.queue.isOverflown():
            self.msgDisplay=True
            self.displayMsg(msg="Queue is full",pos=(300, 220))
        else:
            self.queue.enqueue(random.randint(1, 100))
            self.queueObjects.append(pygame.Surface(self.blockSize, pygame.SRCALPHA))
            if self.msgDisplay:
                self.msgDisplay=False
                self.screen.fill((0, 0, 0), (200, 210, 200, 30))
                
    def displayDequeue(self):
        if self.queue.isUnderflown():
            self.msgDisplay=True
            self.displayMsg(msg="Queue is empty",pos=(300, 220))
        else:
            self.queue.dequeue()
            self.queueObjects.pop(0)
            if self.msgDisplay:
                self.msgDisplay=False
                self.screen.fill((0, 0, 0), (200, 210, 200, 30))
    
    def displayMsg(self,msg, color=(255, 255, 255), pos=(180, 100)):
        text=self.font.render(msg, True, color)
        textRect = text.get_rect()
        textRect.center = pos
        self.screen.blit(text, textRect)
            
if __name__=="__main__":
    QueueVisual().run()