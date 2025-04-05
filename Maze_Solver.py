import pygame 
import numpy as np
import random

WIDTH,HEIGHT = 600,600
CELL_SIZE = 5
GRID_HEIGHT = HEIGHT//CELL_SIZE
GRID_WIDTH = WIDTH//CELL_SIZE 

def busca(mapa, posicao, chegada):
    x, y = posicao
    if posicao == chegada:
        return True
    
    direcoes = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for dx,dy in direcoes:
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or ny < 0 or nx >= len(mapa) or ny >= len(mapa[0]):
            return 
        
        if mapa[nx][ny] == 0:  
            mapa[nx][ny] += 1  
            if busca(mapa, (nx, ny), chegada):
                
                return True  
    
    return False 


def cor(valor):
    if valor == 0:
        return 'black'
    elif valor == -1:
        return 'green'
    else:
        return 'orange' 


def draw_grid(screen,mat): 
    screen.fill('black')
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if mat[i][j] == -1:
                pygame.draw.rect(screen,cor(mat[i][j]),(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE))
            elif mat[i][j] == 0:
                pygame.draw.rect(screen,cor(mat[i][j]),(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE))
            elif mat[i][j] >= 1:
                pygame.draw.rect(screen,cor(mat[i][j]),(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE))

    

def create_grid():
    mapa = np.random.choice([-1,0],size = (GRID_WIDTH,GRID_HEIGHT))
    vazios = []
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if mapa[i][j] == 0:
                vazios.append((i,j))
    posicao = list(random.choice(vazios))
    
    direcoes = [(1,0),(-1,0),(0,1),(0,-1)]
    resolucao = posicao
    xi = resolucao[0]
    yi = resolucao[1]
    while resolucao <= [GRID_HEIGHT,GRID_WIDTH]:
        dir_random = random.choice(direcoes)
        if mapa[xi][yi] == -1:
            mapa[xi][yi] = 0
        xi += dir_random[0]
        yi += dir_random[1]
        if xi >= GRID_HEIGHT or yi >= GRID_WIDTH or xi <= 0 or yi <= 0 :
            if xi >= GRID_HEIGHT:
                xi = GRID_HEIGHT-1
            if xi <= 0:
                xi = 1
            if yi >= GRID_WIDTH:
                yi = GRID_HEIGHT-1
            if  yi <= 0 :
                yi = 1
            break
    return (mapa,[xi,yi],posicao)



def main():
    mapa,chegada,posicao = create_grid()
    x = posicao[0]
    y = posicao[1]
    running = True
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT,WIDTH))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Labirinto')
    busca(mapa,[x,y],chegada)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False          
        draw_grid(screen,mapa)
        pygame.draw.rect(screen,'blue',(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
        pygame.draw.rect(screen,'red',(chegada[0]*CELL_SIZE,chegada[1]*CELL_SIZE,CELL_SIZE,CELL_SIZE))
        pygame.display.flip()
        clock.tick(10)



if __name__ == '__main__':
    main()