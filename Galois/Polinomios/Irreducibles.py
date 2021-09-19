def polinomioIrreducible(M):
	listaPolinomios =[
		[160,1,2,117],[161,18],[162,27],[163,1,2,8],[164,1,2,49],[165,1,2,25],[166,37],[167,6],[168,1,2,65],[169,34],[170,11],[171,1,3,42],[172,1],[173,1,2,10],[174,13],[175,6],[176,1,2,43],[177,8],[178,31],[179,1,2,4],[180,3],[181,1,2,89],[182,81],[183,56],[184,1,2,81],[185,24],[186,11],[187,1,2,20],[188,1,2,60],[189,1,2,49],[190,1,2,47],[191,9],[192,1,2,7],[193,15],[194,87],[195,1,2,37],[196,3],[197,1,2,21],[198,9],[199,34],[200,1,2,81],[201,14],[202,55],[203,1,2,45],[204,27],[205,1,2,21],[206,1,2,63],[207,43],[208,1,2,83],[209,6],[210,7],[211,1,2,165],[212,105],[213,1,2,62],[214,73],[215,23],[216,1,2,107],[217,45],[218,11],[219,1,2,65],[220,7],[221,1,2,18],[222,1,2,73],[223,33],[224,1,2,159],[225,32],[226,1,2,30],[227,1,2,21],[228,113],[229,1,2,21],[230,1,2,13],[231,26],[232,1,2,23],[233,74],[234,31],[235,1,2,45],[236,5],[237,1,2,104],[238,73],[239,36],[240,1,3,49],[241,70],[242,95],[243,1,2,17],[244,111],[245,1,2,37],[246,1,2,11],[247,82],[248,1,2,243],[249,35],[250,103],[251,1,2,45],[252,15],[253,46],[254,1,2,7],[255,52],[256,1,2,155],[257,12],[258,71],[259,1,2,254],[260,15]
	]
	polinomio = listaPolinomios[M-160]
	print(polinomio)
	return polinomio

def PolinomioBinario(M):
	polinomio = polinomioIrreducible(M)
	PolinomioBinario = []

	for i in range(M+1):
		if  i == 0:
			PolinomioBinario.append(1)
		else:
			PolinomioBinario.append(0)


	for i in range(len(polinomio)):
		PolinomioBinario[polinomio[i]] = 1
	return PolinomioBinario
