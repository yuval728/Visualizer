import random
import pygame
import time
import uuid


class Node():
    def __init__(self, value, id=0):
        self.value=value
        self.id=id
        self.left=None
        self.right=None
        
class BinarySearchTree():
    def __init__(self):
        self.root=None
        self.lenght=0
        
    def insert(self, value):
        if self.root==None:
            self.root=Node(value,uuid.uuid1())
            self.lenght+=1
        else:
            temp=self.root
            while temp!=None:
                if value < temp.value:
                    if temp.left==None:
                        temp.left=Node(value,uuid.uuid1())
                        break
                    else:
                        temp=temp.left
                else:
                    if temp.right==None:
                        temp.right=Node(value,uuid.uuid1())
                        break
                    else:
                        temp=temp.right
                        
    def remove(self,root, val, id):
        if root is None:
            return root
        
        
        if root.value>val:
            root.left=self.remove(root.left,val,id)
            return root
        if root.value<val:
            root.right=self.remove(root.right,val,id)
            return root
        
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            succParent=root
            succ=root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
    
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            root.value = succ.value

            del succ
            return root
        
        
    def maxDepth(root, depth):
        if not root: 
            return depth
        
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            
    def inorder(self,root,tree):
        node=root
        if node!=None:
            self.inorder(node.left,tree)
            # print(node.value) 
            tree.append(node.value)
            self.inorder(node.right,tree)
        
    def preorder(self,root,tree):
        node=root
        if node!=None:
            # print(node.value)
            tree.append(node.value)
            self.preorder(node.left,tree)
            self.preorder(node.right,tree)
            
    def postorder(self,root,tree):
        node=root
        if node!=None:
            self.postorder(node.left,tree)
            self.postorder(node.right,tree)
            tree.append(node.value)
            # print(node.value)
            

class BinaryTreeVisual:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 750
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.binaryTree = BinarySearchTree()
        self.binaryTreeObjects=[]
        self.font=pygame.font.SysFont("comicsansms", 20)
        
        self.user_text = ''
        self.binaryTree.insert(5)
        self.binaryTree.insert(2)
        # self.binaryTree.insert(7)
        # self.binaryTree.insert(3)
        # self.binaryTree.insert(1)
        # self.binaryTree.insert(8)
        # self.binaryTree.insert(6)
        # self.binaryTree.insert(3.5)
        # self.binaryTree.insert(1.5)
        # self.binaryTree.insert(8.5)
        # self.binaryTree.insert(6.5)
        # self.binaryTree.insert(5.5)
        # self.binaryTree.insert(2.5)
        # self.binaryTree.insert(7.5)
        # self.binaryTree.insert(0.5)
        
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
        
    def binaryTreeReq(self):
        self.screen.fill((0, 0, 0))
        font=pygame.font.SysFont("comicsansms", 36)
        BTtext = font.render("Binary Tree", True, (255, 255, 255))
        BTtextRect = BTtext.get_rect()
        BTtextRect.center = (self.WIDTH/2, 30)
        self.screen.blit(BTtext, BTtextRect)
        
        self.blockSize = (50, 40)
        self.nodeSize=30
        self.arrowSize=30
        # self.padding=20
        self.binaryTreeObjects=[]
        
        self.displayMsg(msg='Click on the blocks to remove', pos=(self.WIDTH/2+180, self.HEIGHT-150))
        
        inputBox = pygame.Rect(self.WIDTH/2+70, self.HEIGHT-120, 140, 30)
        pygame.draw.rect(self.screen, (255, 255, 255), inputBox)
        font=pygame.font.SysFont("comicsansms", 20)
        text_surface = font.render(self.user_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (inputBox.x+5, inputBox.y))
        inputBox.w = max(200, text_surface.get_width()+10)
        
        
        self.buttons('Insert', (self.WIDTH/2+220, self.HEIGHT-120, 80, 30))
        self.buttons('Reset', (self.WIDTH/2+120, self.HEIGHT-50, 80, 30))
        
        inoderTree=[]
        self.binaryTree.inorder(self.binaryTree.root,inoderTree)
        self.displayMsg(msg='Inorder: '+str(inoderTree), pos=(100+len(inoderTree)*10, self.HEIGHT-100))
        
        preoderTree=[]
        self.binaryTree.preorder(self.binaryTree.root,preoderTree)
        self.displayMsg(msg='Preorder: '+str(preoderTree), pos=(100+len(inoderTree)*10, self.HEIGHT-70))
        
        postoderTree=[]
        self.binaryTree.postorder(self.binaryTree.root,postoderTree)
        self.displayMsg(msg='Postorder: '+str(postoderTree), pos=(100+len(inoderTree)*10, self.HEIGHT-40))
        
    
    def drawBinaryTree(self, surface, node, x, y, horizontal_distance=150):
        
        if node:
            self.binaryTreeObjects.append((pygame.Surface((x+self.blockSize[0],y+self.blockSize[1]), pygame.SRCALPHA), self.i,(node.id,node.value),(x,y)))
            
            pygame.draw.circle(self.binaryTreeObjects[self.i][0], (255, 255, 255), (self.blockSize[0],self.blockSize[1]+self.arrowSize), self.nodeSize-5)

            text = self.font.render(str(node.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.blockSize[0],self.blockSize[1]+self.nodeSize))
            self.binaryTreeObjects[self.i][0].blit(text, text_rect)
            
            
            #!Not working
            # if node.left:
                # pygame.draw.line(self.binaryTreeObjects[self.i][0], (255, 255, 255), (x-self.blockSize[0], self.blockSize[1]+self.arrowSize), (x - horizontal_distance, y + self.arrowSize+self.blockSize[1]+self.nodeSize), 5)
                
                
            # if node.right:
                # pygame.draw.line(self.binaryTreeObjects[self.i][0], (255, 255, 255), (self.blockSize[0], self.blockSize[1]+self.arrowSize), (x + horizontal_distance, y + self.arrowSize+self.blockSize[1]+self.nodeSize), 5)
            
            self.screen.blit(self.binaryTreeObjects[self.i][0], (x ,y))
            
            self.i+=1
            if node.left: 
                
                self.drawBinaryTree(self.i, node.left, x - horizontal_distance, y + self.arrowSize+self.blockSize[1]+self.nodeSize, horizontal_distance / 2)

            if node.right:
                
                self.drawBinaryTree(self.i, node.right, x + horizontal_distance, y + self.arrowSize+self.blockSize[1]+self.nodeSize, horizontal_distance / 2)


        
    def run(self):
        done=False
        
        while not done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done=True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mpos = pygame.mouse.get_pos()
                        self.checkRemoveClick(mpos)
                        
                        if self.WIDTH/2+120<mpos[0]<self.WIDTH/2+200 and self.HEIGHT-50<mpos[1]<self.HEIGHT-20:
                            self.binaryTree=BinarySearchTree()
                        if self.WIDTH/2+220<mpos[0]<self.WIDTH/2+300 and self.HEIGHT-120<mpos[1]<self.HEIGHT-90:
                            self.binaryTree.insert(int(self.user_text))
                            self.user_text=''

                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.binaryTree=BinarySearchTree()
                    if event.key == pygame.K_BACKSPACE: 
                        self.user_text = self.user_text[:-1] 
                    else: 
                        if event.unicode.isnumeric():
                            self.user_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        self.binaryTree.insert(int(self.user_text))
                        self.user_text=''
        
            self.binaryTreeReq()
            self.i=0
            self.drawBinaryTree(self.i,self.binaryTree.root,self.WIDTH/2-self.blockSize[0],100)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        
    def checkRemoveClick(self,mpos):
        for i in self.binaryTreeObjects:
            # print(i[0].get_rect(),mpos)
            if i[0].get_rect(topleft=self.blockSize).collidepoint(mpos):
                # print(i[2][1])
                self.binaryTree.remove(self.binaryTree.root, i[2][1], i[2][0])
                break
        
        

if __name__=='__main__':
    btv=BinaryTreeVisual()
    btv.run()
    
