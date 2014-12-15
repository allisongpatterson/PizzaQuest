SPRITES =  {'c1' : '1_corner.gif',
			'c2' : '2_corner.gif',
			'c3' : '3_corner.gif',
			'c4' : '4_corner.gif',
			'hw' : 'H_wall.gif',
			'vw' : 'V_wall.gif',
			#'rb' : 'reg_barricade.gif', 
			'bu' : 'bush.gif',
			#'tr' : 'tree.gif',
			'fl' : 'flower.gif',
			#'pa' : 'path.gif'
			}

LEVELS = [[0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu',
		   0000, 'bu', 0000, 'c1', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'c2', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000,
		   0000, 'fl', 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'fl', 'c4', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'c3', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'fl', 0000, 'bu', 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 'fl', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'bu', 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'c1', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw', 'hw',
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'bu', 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
		   'bu', 0000, 0000, 0000, 'fl', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 'vw', 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000]]