import rclpy, math, time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .laser import LaserSub

class VelocidadePub(Node):

    def __init__(self):
        # Criar publisher
        super().__init__('velocidadepub')
        self.velocity_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.movimenta)
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 0.0  
        self.vel_msg.linear.y = 0.0 
        self.vel_msg.linear.z = 0.0  
        self.vel_msg.angular.x = 0.0
        self.vel_msg.angular.y = 0.0  
        self.vel_msg.angular.z = 0.0
        self.get_logger().info('criou publisher!!')

    # def movimenta(self, tem_parede):
    #     if(tem_parede):
    #         #self.para()
    #         self.viraEsquerda()
    #     else:
    #         self.andaFrente()
    #         #self.andaEsquerda()

    # def movimenta(self, tipoMovimento):
    #     if(tipoMovimento == 1):
    #         self.andaFrente()
    #     elif(tipoMovimento == 2):
    #         self.andaEsquerda()
    #     elif(tipoMovimento == 3):
    #         self.andaDireita()
    #     elif(tipoMovimento == 4):
    #         self.viraEsquerda()
    #     elif(tipoMovimento == 5):
    #         self.viraDireita()

        # if(tem_parede_frente and vira_esquerda):
        #     self.viraEsquerda()
        # elif(tem_parede_frente and vira_direita):
        #     self.viraDireita()
        # elif(vira_esquerda):
        #     self.andaEsquerda()
        # elif(vira_direita):
        #     self.andaDireita()
        # else:
        #     self.andaFrente()

    # def para(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.0
    #     move_cmd.angular.z = 0.0

    #     print(self.velocity_publisher)
    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Parado.')

    # def andaFrente(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.1
    #     move_cmd.angular.z = 0.0

    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Andando para frente com velocidade 0.1')

    # def andaEsquerda(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.1
    #     move_cmd.angular.z = 0.1

    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Andando para esquerda com velocidade 0.1')

    # def andaDireita(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.1
    #     move_cmd.angular.z = -0.1

    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Andando para direita com velocidade 0.1')

    # def viraEsquerda(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.0
    #     move_cmd.angular.z = 0.1

    #     print(self.velocity_publisher)
    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Virando para esquerda com velocidade 0.1')

    # def viraDireita(self):
    #     move_cmd = Twist()
    #     move_cmd.linear.x = 0.0
    #     move_cmd.angular.z = -0.1

    #     self.velocity_publisher.publish(move_cmd)
    #     self.get_logger().info('Virando para direita com velocidade 0.1')

def movimenta(velocity_publisher, tipoMovimento):
    print('bateu no movimenta! tipoMovimento: ', tipoMovimento)
    if(tipoMovimento == 1):
        andaFrente(velocity_publisher)
    elif(tipoMovimento == 2):
        andaEsquerda(velocity_publisher)
    elif(tipoMovimento == 3):
        andaDireita(velocity_publisher)
    elif(tipoMovimento == 4):
        print('chamando viraEsquerda...')
        viraEsquerda(velocity_publisher)
    elif(tipoMovimento == 5):
        viraDireita(velocity_publisher)

def andaFrente(velocity_publisher):
    move_cmd = Twist()
    move_cmd.linear.x = 0.1
    move_cmd.angular.z = 0.0

    velocity_publisher.publish(move_cmd)
    get_logger().info('Andando para frente com velocidade 0.1')

def andaEsquerda(velocity_publisher):
    move_cmd = Twist()
    move_cmd.linear.x = 0.1
    move_cmd.angular.z = 0.1

    velocity_publisher.publish(move_cmd)
    get_logger().info('Andando para esquerda com velocidade 0.1')

def andaDireita(velocity_publisher):
    move_cmd = Twist()
    move_cmd.linear.x = 0.1
    move_cmd.angular.z = -0.1

    velocity_publisher.publish(move_cmd)
    get_logger().info('Andando para direita com velocidade 0.1')

def viraEsquerda(velocity_publisher):
    move_cmd = Twist()
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.1

    print('enviando comando...')
    velocity_publisher.publish(move_cmd)
    print('Virando para esquerda com velocidade 0.1')

def viraDireita(velocity_publisher):
    move_cmd = Twist()
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = -0.1

    velocity_publisher.publish(move_cmd)
    get_logger().info('Virando para direita com velocidade 0.1')


def main(args=None):
    rclpy.init(args=args)

    laser = LaserSub()
    #velocidade = VelocidadePub()
    vel = rclpy.create_node('velocidadepub')
    velocity_publisher = vel.create_publisher(Twist, 'cmd_vel', 10)
    timer_period = 0.01
    timer = vel.create_timer(timer_period, movimenta)
    vel_msg = Twist()
    vel_msg.linear.x = 0.0  
    vel_msg.linear.y = 0.0 
    vel_msg.linear.z = 0.0  
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0  
    vel_msg.angular.z = 0.0
    print('criou pub')


    ultimoMov = 1
    contLoop = 0
    while(True):
        rclpy.spin_once(laser)
        print('sudoeste: ', str(laser.sudoeste))
        print('oeste: ', str(laser.oeste))
        print('noroeste: ', str(laser.noroeste))
        print('norte: ', str(laser.norte))
        print('nordeste: ', str(laser.nordeste))
        print('leste: ', str(laser.leste))
        print('sudeste: ', str(laser.sudeste))

        andarEsquerda = 2
        andarDireita = 3
        virarEsquerda = 4
        virarDireita = 5

        tipoMovimento = 1 #andar pra frente

        seguroOeste = (laser.oeste > 0.4 and laser.oeste != 0.0) or laser.oeste == math.inf
        seguroNoroeste = (laser.noroeste > 0.4 and laser.noroeste != 0.0) or laser.noroeste == math.inf
        seguroNorte = (laser.norte > 0.4 and laser.norte != 0.0) or laser.norte == math.inf
        seguroNordeste = (laser.nordeste > 0.4 and laser.nordeste != 0.0) or laser.nordeste == math.inf
        seguroLeste = (laser.leste > 0.4 and laser.leste != 0.0) or laser.leste == math.inf
        

        tratouPerigo = False
        if(seguroNorte == False):
            tipoMovimento = virarDireita
            tratouPerigo = True

        if(seguroNoroeste == False):
            tipoMovimento = virarDireita
            tratouPerigo = True
        if(seguroNordeste == False):
            tipoMovimento = virarEsquerda
            tratouPerigo = True

        if(tratouPerigo == False and seguroLeste == False):
            tipoMovimento = andarEsquerda
            tratouPerigo = True
        if(tratouPerigo == False and seguroOeste == False):
            tipoMovimento = andarDireita
            tratouPerigo = True

        print('tratouPerigo:', tratouPerigo)
        print('tipoMovimento:', tipoMovimento)
        print('contLoop:', contLoop)
        if(tratouPerigo and (ultimoMov != 1) and 
            (ultimoMov != andarEsquerda) and 
            (ultimoMov != andarDireita) and 
            (tipoMovimento != ultimoMov)):
            print('Corrigiu!')
            tipoMovimento = ultimoMov

        

        # if(tratouPerigo == False and (contLoop % 4) == 0):
        #     #faz ajustes finos

        #     if(laser.noroeste != 0.0 and laser.nordeste != 0.0):
        #         if(laser.noroeste > laser.nordeste and (laser.noroeste - laser.nordeste) >= 1.5):
        #             print('ajuste fino para esquerda...');
        #             tipoMovimento = andarEsquerda
        #         elif(laser.nordeste > laser.noroeste and (laser.nordeste - laser.noroeste) >= 1.5):
        #             print('ajuste fino para direita...');
        #             tipoMovimento = andarDireita



        ultimoMov = tipoMovimento
        contLoop += 1
        #velocidade.movimenta(tipoMovimento)
        print('chamando movimenta com tipo de movimento = ', tipoMovimento)
        movimenta(velocity_publisher, tipoMovimento)
        
        # if( (laser.norte < 0.4 and laser.norte != 0.0) or
        #     (laser.noroeste < 0.5 and laser.noroeste != 0.0) or 
        #     (laser.nordeste < 0.4 and laser.nordeste != 0.0)):
        #     tem_parede = 1
        #     print("Distância da parede: ", str(laser.norte))
        #     print("com parede à frente")
        # else:
        #     tem_parede = 0
        #     print("sem parede à frente")

        #velocidade.movimenta(tem_parede)
            
if __name__ == '__main__':
    main()
