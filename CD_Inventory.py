#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (DTsakalos, 2021-Mar-07, Added code in place of pseudocode)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


# -- CD Track Data -- #
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD

    methods:
        __str__: -> (string) with cd_id, cd_title, cd_artist formatted for screen display
        file_str: -> (string) with cd_id, cd_title, cd_artist formatted for saving to file
    """

    ###    Contructor    ###
    def __init__(self, cd_id, cd_title, cd_artist):

        ###    Attributes    ###
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    ###    Properties    ####
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, cd_id):
        if type(cd_id) == int:
            self.__cd_id = cd_id
        else:
            raise Exception('CD ID must be an integer')

    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, cd_title):
        if type(cd_title) == str:
            self.__cd_title = cd_title
        else:
            raise Exception('CD Title must be a string')

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, cd_artist):
        if type(cd_artist) == str:
            self.__cd_artist = cd_artist
        else:
            raise Exception('CD Artist must be a string')

    ###    Methods    ###
    def __str__(self):
        return '{}.\t\t{}\t\t\t\t(by: {})'.format(self.cd_id, self.cd_title, self.cd_artist) # using getter

    def file_str(self):
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist) # using getter



# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

    ###    Methods    ###
    def save_inventory(self, file_name, lst_Inventory):
        objFile = open(file_name, 'w')
        for track in lst_Inventory:
            objFile.write(track.file_str())
        objFile.close()

    def load_inventory(self, file_name):
        lst_Inventory = []
        while True:
            try:
                objFile = open(file_name, 'r')
                break
            except FileNotFoundError:
                objFile = open(file_name, 'w')
                print('No previous file found. Created an empty file!')
        for line in objFile:
            data = line.strip().split(',')
            track = CD(int(data[0]), data[1], data[2]) # using constructor
            lst_Inventory.append(track)
        objFile.close()
        return lst_Inventory



# -- PRESENTATION (Input/Output) -- #
class IO:
    """ Presents the information to use and collects input:
        
        methods: 
            print_menu: Prints menu for user -> None
            menu_choice: -> (string) of the choice the user selects
            show_inventory(table): (string) Prints a list of Objects -> None
            load_choice: -> (boolean) to notify of data loss if loading
            get_new_cd_data: -> (object) of the data relating to the song -> None
    """

    ###    Methods    ###
    #show menu to user
    @staticmethod
    def print_menu():
        print('\n------------Menu------------')
        print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    #captures user's choice
    @staticmethod
    def menu_choice():
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    #display the current data on screen
    @staticmethod
    def show_inventory(table):
        print('\n======= The Current Inventory: =======')
        print('ID\t\t CD Title \t\t (by: Artist)')
        print('======================================')
        for track in table:
            print(track)
        print('======================================')

    #allow user to load
    @staticmethod
    def load_choice():
        load_file = False
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            load_file = True
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        return load_file

    #get CD data from user
    @staticmethod
    def get_new_cd_data():
            # 3.3.1 Ask user for new ID, CD Title and Artist
        while True:
            try:
                intID = int(input('Enter an ID: ').strip())
                break
            except ValueError: #making sure the program does not crash with string as input
                print('Invalid Input! Try again.')
        while True:
            try:
                strTitle = input('What is the CD\'s title? ').strip()
                if strTitle == '':
                    raise ValueError()
                break
            except ValueError: #making sure the program does not contain empty string
                print('Invalid Input! Try again.')
        while True:
            try:
                strArtist = input('What is the Artist\'s name? ').strip()
                if strArtist == '':
                    raise ValueError()
                break
            except ValueError: #making sure the program does not contain empty string
                print('Invalid Input! Try again.')
        track = CD(intID, strTitle, strArtist)
        return track

# -- Main Body of Script -- #

# 1. Load data from file into a list of CD objects on script start
fileIO_obj = FileIO()
lstOfCDObjects = fileIO_obj.load_inventory(strFileName)

# 2. Display menu to user
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break

    # 3.2 process load inventory
    if strChoice == 'l':
        reload_file = IO.load_choice()
        if reload_file:
            lstOfCDObjects = fileIO_obj.load_inventory(strFileName)
        IO.show_inventory(lstOfCDObjects)

    # 3.3 process add a CD
    elif strChoice == 'a':
        track = IO.get_new_cd_data()
        lstOfCDObjects.append(track)
        IO.show_inventory(lstOfCDObjects)

    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)

    # 3.5 process save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.5.2 Process choice
        if strYesNo == 'y':
            fileIO_obj.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')
