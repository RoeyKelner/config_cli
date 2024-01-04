import xml.etree.ElementTree as ET

CONFIG_XML_PATH = "D:\\Users\\rkelner\\source\\MfgTools\\src\\config.xml"




def main():
    role_dict = {'CONSOLE' : 'Contoller', 'DUT' : 'DUT'}
    tree = ET.parse(CONFIG_XML_PATH)
    root = tree.getroot()
    print(f'Editing conf file at: {CONFIG_XML_PATH}\n')

    for entity in root.iter('GenericEntity'):
        role = role_dict[entity.find('Role').text]
        set_ip(role, entity)
        set_password(entity, role)

    keep_current_or_set_new(root.find('.//PlatformFamily'), 'Platform Family')
    keep_current_or_set_new(root.find('.//KitVersion'), 'Kit Version')
    keep_current_or_set_new(root.find('.//SystemToolsPath'), 'Tools Path')
    keep_current_or_set_new(root.find('.//ImagePath'), 'Image Path')
    keep_current_or_set_new(root.find('.//FwSku'), 'FwSku')


    tree.write(CONFIG_XML_PATH)

def keep_current_or_set_new(elem, elem_name):
    usr_input = input(f'Current {elem_name} is {elem.text} [Hit <Enter> to confirm or type a new one]:\n')
    elem.text = elem.text if usr_input == '' else usr_input

def set_ip(role : str, entity_elem):
    ip_elem = entity_elem.find('.//IpAddress')
    print(f'     ----+  {role}  +----')
    ip_input = input(f'Current IP: {ip_elem.text} [<Enter> to confirm or type a new one]:\n')
    if ip_input == '':
        ip_input = ip_elem.text
    if ip_input == '1':
        ip_input = '1.1.1.1'
    ip_elem.text = ip_input

def set_password(elem, role):
    usr_input = input(f'{role} Password - hit <Enter> for P@ssw0rd or type \'1\' for Admin!98:\n')
    password_elem = elem.find('.//Password')
    password_elem.text = 'P@ssw0rd' if usr_input == '' else 'Admin!98'


if __name__ == '__main__':
    main()
