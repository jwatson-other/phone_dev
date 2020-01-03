# ~~ Constants ~~
N=0; E=1; S=2; W=3; U=4; D=5;
_MOV = [
	(0,1,0),  (1,0,0),  (0,-1,0),  (-1,0,0),
	(0,0,1),  (0,0,-1),
]

# ~~ Classes ~~

class Room:
	" location base class "
	def __init__( self ):
		self.doors = [ None for i in range(6) ]
		self.nside = []
	def add_door( self , i , ref ):
		self.doors[i] = ref

class Mob:
	" mobile entity base class "
	def __init__( self , HP , room=None ):
		self.hp = HP
		self.loc = room
		self.id = "Mob"
	def move(self, i):
		if self.loc[i] != None:
			self.loc 
		
# ~~~~ Main Loop ~~~~
if __name__ == '__main__':
	print('BEGIN')
	print('END')