import pygame
import random
import time



class Node:
    def __init__(self, item):
        # self.id = globalid
        self.item = item
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.length = 1
        
    def add(self, item, head=False, tail=False, pos=0):
        try:
            
            # if pos > self.length:
            #     return None 
            if self.length>6:
                return None
            if self.head == None:
                self.head = Node(item)
                
            # elif pos <= 0:
            elif head:
                temp = self.head
                self.head = Node(item)
                self.head.next = temp
                
            # elif pos == self.length:
            elif tail:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = Node(item)
                temp = temp.next
                
            else:
                temp = self.head
                for i in range(pos-1):
                    temp = temp.next
                node=Node(item)
                node.next = temp.next
                temp.next = node
                
                
            self.length += 1
        except Exception as e:
            print(e)
            return None
    
    def remove(self, pos):
        if self.head == None:
            return None
        
        temp = self.head
        if pos == 0:
            self.head = temp.next
        else:
            for i in range(pos-1):
                temp = temp.next
            temp.next = temp.next.next
            
        self.length -= 1
            
    
    def getall(self):
        temp = self.head
        while temp != None:
            yield temp.item
            temp = temp.next
            
    def getLength(self):
        return self.length
    
    def reset(self):
        self.head = None
        self.length = 1

class LinkedListVisual():
    def __init__(self):
        
        pygame.init()
        self.WIDTH = 1000
        self.HEIGHT = 450
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.linkedList = LinkedList()
        # self.linkedList.add(1,1,0)
        # self.linkedList.add(2,2,1)
        # self.linkedList.add(3,3,2)
        
        self.linkedListObjects = []
        self.linkedListArrowObjects = []
        self.font=pygame.font.SysFont("comicsansms", 20)
        
    def displayMsg(self,msg, color=(255, 255, 255), pos=(180, 100)):
        text=self.font.render(msg, True, color)
        textRect = text.get_rect()
        textRect.center = pos
        self.screen.blit(text, textRect)
        
    def buttons(self, placeHolder, coordinates):
        font=pygame.font.SysFont("comicsansms", 20)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(coordinates))
        text=font.render(placeHolder, True, (10, 10, 10))
        textRect = text.get_rect()
        textRect.center = (coordinates[0]+coordinates[2]/2, coordinates[1]+coordinates[3]/2)
        self.screen.blit(text, textRect)
    
    def drawAdd(self,pos):
        if self.linkedList.length>7:
            return None
        self.linkedList.add(random.randint(1,10), pos=pos)
    
    def drawRemove(self,pos):
        if self.linkedList.length<2:
            return None
        self.linkedList.remove(pos)
    
    def linkedListReq(self):
        self.screen.fill((0, 0, 0))
        font=pygame.font.SysFont("comicsansms", 36)
        lltext = font.render("Linked List", True, (255, 255, 255))
        lltextRect = lltext.get_rect()
        lltextRect.center = (self.WIDTH/2, 30)
        self.screen.blit(lltext, lltextRect)
        
        self.blockSize = (100, 50)
        self.linkedListBlockPosition=(30, self.HEIGHT/2-self.blockSize[1]*2)
        self.arrowSize = (60, 10)
        
        headText=self.font.render("Head", True, (255, 255, 255))
        headTextRect = headText.get_rect()
        headTextRect.center = (self.linkedListBlockPosition[0], self.linkedListBlockPosition[1]-self.blockSize[1]/2)
        self.screen.blit(headText, headTextRect)
        
        self.buttons("Add Head", (self.WIDTH/2-80, self.HEIGHT-180, 100, 30))
        self.buttons("Add Tail", (self.WIDTH/2-80, self.HEIGHT-130, 100, 30))
        self.buttons("Reset", (self.WIDTH/2-80, self.HEIGHT-80, 100, 30))
        
        self.displayMsg(msg='Press Space to add at Head', pos=(self.WIDTH/2-300, self.HEIGHT-170))
        self.displayMsg(msg='Press Enter to add at Tail', pos=(self.WIDTH/2-300, self.HEIGHT-120))
        self.displayMsg(msg='Press Esc to reset', pos=(self.WIDTH/2-300, self.HEIGHT-70))
        
        self.displayMsg(msg='Click on the blocks to remove', pos=(self.WIDTH/2+200, self.HEIGHT-150))
        self.displayMsg(msg='Click on line to add', pos=(self.WIDTH/2+200, self.HEIGHT-100))
        
    def drawLinkedList(self):
        
        self.linkedListObjects = []
        self.linkedListArrowObjects = []
        for i, item in enumerate(self.linkedList.getall()):
            self.linkedListObjects.append((pygame.Surface(self.blockSize, pygame.SRCALPHA), i))
            
            pygame.draw.rect(self.linkedListObjects[i][0], (250, 250, 250), pygame.Rect(5,0, self.blockSize[0]-10, self.blockSize[1]), 2)            
            pygame.draw.line(self.linkedListObjects[i][0], (250, 250, 250), (self.blockSize[0]-40, 0), (self.blockSize[0]-40, self.blockSize[1]), 2)
            pygame.draw.circle(self.linkedListObjects[i][0], (250, 250, 250), (self.blockSize[0]-20, 12), 6)
            
            
            self.linkedListArrowObjects.append((pygame.Surface(self.arrowSize, pygame.SRCALPHA), i))
            
            pygame.draw.circle(self.linkedListArrowObjects[i][0], (255, 255, 250), (5, self.arrowSize[1]/2), 6)
            pygame.draw.circle(self.linkedListArrowObjects[i][0], (250, 250, 250), (self.arrowSize[0]-5, self.arrowSize[1]/2), 6)
            pygame.draw.line(self.linkedListArrowObjects[i][0], (250, 250, 250), (0, self.arrowSize[1]/2), (self.arrowSize[0], self.arrowSize[1]/2), 3)
            
            text=self.font.render(str(item), True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (self.blockSize[0]/2-12, self.blockSize[1]/2)
            self.linkedListObjects[i][0].blit(text, textRect)
            
            addText=self.font.render("+", True, (0,0,0))
            addTextRect1 = addText.get_rect()
            addTextRect1.center = (self.arrowSize[0]-5, self.arrowSize[1]/2-2)
            self.linkedListArrowObjects[i][0].blit(addText, addTextRect1)
            
            addText2=self.font.render("+", True, (0,0,0))
            addTextRect2 = addText2.get_rect()
            addTextRect2.center = (5, self.arrowSize[1]/2-2)
            self.linkedListArrowObjects[i][0].blit(addText2, addTextRect2)
            
            removeText=self.font.render("x", True, (0,0,0))
            removeTextRect = removeText.get_rect()
            removeTextRect.center = (self.blockSize[0]-20, 9)
            self.linkedListObjects[i][0].blit(removeText, removeTextRect)
            
    
            self.screen.blit(self.linkedListObjects[i][0], (self.linkedListBlockPosition[0]+i*(self.blockSize[0]+self.arrowSize[0]), self.linkedListBlockPosition[1]))
            if i != 0:
                self.screen.blit(self.linkedListArrowObjects[i-1][0], (self.linkedListBlockPosition[0]+(i-1)*(self.blockSize[0]+self.arrowSize[0])+self.blockSize[0], self.linkedListBlockPosition[1]+self.blockSize[1]/2-self.arrowSize[1]/2))
                
        if self.linkedList.length>1:
            tailText=self.font.render("Tail", True, (255, 255, 255))
            tailTextRect = tailText.get_rect()
            tailTextRect.center = (self.linkedListBlockPosition[0]+(self.linkedList.length-1)*(self.blockSize[0]+self.arrowSize[0])-30, self.linkedListBlockPosition[1]-self.blockSize[1]/2)
            self.screen.blit(tailText, tailTextRect)
            
        
    def run(self):
        done=False
        
        while not done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mpos = pygame.mouse.get_pos()
                        
                        self.checkAddClick(mpos)
                        self.checkRemoveClick(mpos)
                        
                        if self.WIDTH/2-80<mpos[0]<self.WIDTH/2-80+100:
                            if self.HEIGHT-180<mpos[1]<self.HEIGHT-180+30:
                                self.linkedList.add(random.randint(1,10), head=True)
                            if self.HEIGHT-130<mpos[1]<self.HEIGHT-130+30:
                                self.linkedList.add(random.randint(1,10), tail=True)
                            if self.HEIGHT-80<mpos[1]<self.HEIGHT-80+30:
                                self.linkedList.reset()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.linkedList.add(random.randint(1,10), head=True)
                    if event.key == pygame.K_RETURN:
                        self.linkedList.add(random.randint(1,10), tail=True)
                    if event.key == pygame.K_ESCAPE:
                        self.linkedList.reset()
        
            self.linkedListReq()
            self.drawLinkedList()
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()

    def checkAddClick(self, mpos):
        
        for i in self.linkedListArrowObjects:
            if i[0].get_rect(topleft=(self.linkedListBlockPosition[0]+(i[1]-1)*(self.blockSize[0]+self.arrowSize[0])+self.blockSize[0], self.linkedListBlockPosition[1]+self.blockSize[1]/2-self.arrowSize[1]/2)).collidepoint(mpos):
                self.drawAdd(i[1])
                break
            
    def checkRemoveClick(self,mpos):
        
        for i in self.linkedListObjects:
            if i[0].get_rect(topleft=(self.linkedListBlockPosition[0]+(i[1])*(self.blockSize[0]+self.arrowSize[0]), self.linkedListBlockPosition[1])).collidepoint(mpos):
                self.drawRemove(i[1])
                break

if __name__ == "__main__":
    llv = LinkedListVisual()
    llv.run()