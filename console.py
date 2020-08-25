from utils import bash_command

def main():

    print(r"""
            
            ( )
             H
             H
            _H_  
        .-'-.-'-.
        /         |
        |           |
        |   .-------'._
        |  / /  '.' '. |
        |  \ \ @   @ / / 
        |   '---------'      .-------------------------.  
        |    _______|       (     Evil Twin Attack       )
        |  .'-+-+-+|        ( Elmalem Lioz && Caspi Gal  ) 
        |  '.-+-+-+|         '-------------------------'
        |    '''''' |
        '-.__   __.-'
            '''
               
            """)

    upstream_interface_choose = input('\nEnter the upstream interface\n')

    phys_interface_choose = input('\nEnter the access point interface\n')
    
    channel_choose = input('\nEnter the channel\n')
    
    ssid_choose = input('\nEnter the ssid\n')
    
    bash_command('xterm -e python3 program.py -u {0} -i {1} -c {2} -s {3} &'.format(upstream_interface_choose , phys_interface_choose , channel_choose , ssid_choose))

if __name__ == '__main__':
    main()