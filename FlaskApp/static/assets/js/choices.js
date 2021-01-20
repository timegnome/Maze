var options ={0:[1], 1: [20,26,41,21], 2: [29,22,12], 3: [18,9],	4: [44,29,15,11,16,24,43],
	5: [43,22,30,20], 6: [40],	7: [33,36,16],	8: [31,6,29,12], 9: [3,18],	10: [34,41,14],
	11: [40,24],	12: [2,21,8,39],	13: [27,18,25],	14: [10,43,24],	15: [30,37,3],
	16: [36,7],	17: [6,33],	18: [13,3],	19: [31,11],	20: [5,27,1],	21: [44,24,31],
	22: [43,38],	23: [28,8,45,19],	24: [],	25: [34,13,35],	26: [30,36,38,1],
	27: [13,9],	28: [23,43,45,32],	29: [8,40,35,2],	30: [42,34,5,15],	31: [44,19,21],
	32: [11,6,16,28],	33: [3,35,7],	34: [10,25],	35: [33],	36: [7,16],
	37: [15,10,42,20],	38: [40,22,43],	39: [11,4,12],	40: [11,6,38],	41: [1,35,10,38],
	42: [22,30,4,25,37],	43: [22,38],	44: [21,18],	45: [28,17,36,19,23]}

	
// console.log(room)
// console.log(parseInt(room))
// console.log(text)
var context = d3.select('#context')
context.html('')
context.append('p')
.html(`${text}`)

// var location = d3.select('#location')
// location.html('')
// location.image(`FlaskApp/static/assets/images/location/PXL_20210114_215802843.jpg`)

choices = d3.select('#options')
.html('');
options[parseInt(room)].forEach(x => {
	choices.append('div')
	.attr('class',`col-${12/options[parseInt(room)].length}-md boxed`)
	.append('a')
	.attr('id',x)
	.attr('href', `/maze-${x}`)
	.html(`${x}`)
});

