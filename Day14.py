'''
--- Day 14: Disk Defragmentation ---

Suddenly, a scheduled job activates the system's disk defragmenter. Were the situation different, you might sit and watch it for a while, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.

The disk in question consists of a 128x128 grid; each square of the grid is either free or used. On this disk, the state of the grid is tracked by the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, and a number from 0 to 127 corresponding to the row. For example, if your key string were flqrgnkx, then the first row would be given by the bits of the knot hash of flqrgnkx-0, the second row from the bits of the knot hash of flqrgnkx-1, and so on until the last row, flqrgnkx-127.

The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: 0 becomes 0000, 1 becomes 0001, e becomes 1110, f becomes 1111, and so on; a hash that begins with a0c2017... in hexadecimal would begin with 10100000110000100000000101110000... in binary.

Continuing this process, the first 8 rows and columns for key flqrgnkx appear as follows, using # to denote used squares, and . to denote free ones:

##.#.#..-->
.#.#.#.#   
....#.#.   
#.#.##.#   
.##.#...   
##..#..#   
.#...#..   
##.#.##.-->
|      |   
V      V   
In this example, 8108 squares are used across the entire 128x128 grid.

Given your actual key string, how many squares are used?

Your puzzle input was jzgqcdpd.

Your puzzle answer was 8074.
'''
def diskDefragmentationP1(n):
	inputs = []
	for i in range(128):
		inputs.append(n+"-"+str(i))

	hashes = ['7bd6e074b46be65cb4876aae96545d34', 'b53f5f98200ad3323d58fb9165a6c18b', 'da410b6eb19517bad150865916a933a5', 'd069a7ca568f8d473c5806d09882224d', '5d8e518f016a8b2f87f3298fcc093ce9', 'cbf7131a094822e7869fe68ae705c0e6', 'a0ffd078e72a1ca55b0e6c6240b0765e', '18263142dd187843a1a073157f53c43c', 'a389beb5a020bacbdfb2a7e0274bdc4a', 'd5234fd0d0b239a86e1318e5f38d492d', '24c7439f99e0a7f6574bbee521bd6ea2', 'c99873818c9bf2dcc5eb93e2ecd841b0', 'c1cb41bdf13af897c08386a0f31d7fa6', '82297b904fdbfab7040d93c3d22d053a', '350b013d3352968fc6f4a8e320ad5ad4', '77ddfc0a1cb7e37d36182f58e1b7fc9a', '0ca7c37641ca933b09e9891bbe70ec6d', '22af75be22ce3fb6ab4023826c56386b', 'a6477adc855f5956a2980cd65a50c6be', '5a6ab76aa7ee2e2b058c2f8a108bdfc9', 'd0ea8e3178f901a77350ecbc134f1c91', '5137793cc3fcb613b285d13bcdf55b07', 'c8042ea891f17c1937cdab7f09b57da0', '88bdff667431bab4f48e49bc2459dfca', '6072168cc9bfa8df4d50802880a4afb7', 'ed526f0de154c581c102be4c4c6591a5', '80fa45b4f7d89bedd65ef9a025808620', '380518bdb443582170dc4270224cb157', '55028011c2bb307314b19f5a1ce395f6', 'cc0f987cd0f8fe3ebb39175489770bfb', '72b4813165c1db1a4c469da76b843df1', 'd4604c2740a91db29af53fbddee51e51', '1a756b899355b2cb259f94a655ea6663', '5166858290345b19b795ef3a3743580d', '77dd6566f3ca0b93e7922290616b08cd', '05b256a648dc7d0bb94fb7b076e18142', '055af0f9d9a370c9e0dae8ac95423408', '362894f23c2f5992b79de4c09033dfd2', 'f09b7dec160d50442c43118110afd267', 'b82c3adfaf1932ff899fc6ff2969bcd9', '13fcf2a4f9e2efc6a158cc99ecb9b3c1', '5267e8b6a3e542dbb7dc42bf4b24e9a4', 'f20e1ca91c491308d73962785683efc9', 'dae96a9d71a80215e2a2097e832da132', '15fc31a9a64b719ac2463da6cf1117a1', '4f1e6b05af0026dbbf97ac2a394ad969', '27c7d592d6db1df695e85fcb15c56c14', 'a9c2ce40b85cf7f093cc42e2fa675733', 'dac51dabfa78a2b25b4875d1748adaa8', '8c992a2c2a41ed0305aef16432528d45', 'f77ab846a9a157e55dafca60d3cdd956', 'fa8588b29d29bc435d40a101e899ca08', '9eb4ef941c7501d55a6b14a29aa55703', '86a50cd2b86d3957373a53c41ddbe0fa', '1f94a471131d598881ab85d58ab426e3', '906381abd01558900b2cc10331b303b0', 'a6b84c384000f97d62bfea54341b2ac8', '58ba35cfd96686aea5ba8bb70e42b858', 'a7c3c19e7e2484c3702c812ae82e4453', '921465c6a697c1daab196294c5ffe190', '924b56d7e11bb60acf155de616464a65', '111cd1885243955c85b2d053235a7f3e', 'b0d6af9f24f2bd235cd137b96b226f3b', '29187adf2154f9f71bedeaeadc511c88', '668a576715132c6195047cf52fd5daaf', 'c2b7a70332c5793177bbf06a5d9e7c87', '965b0d91596a590c8b83df1ddab8f966', '9417368703f03b2604f9cf5784a7e47e', 'f2fd2dc7c7b7045970d6f92ef6b71de5', 'c103dcce9b765d805c868ccddcbe5a43', '888c0491709d9822114828517c0ae575', 'd23491cc1a10efb2443ea34b80f14c43', '580be6a8b2aff83d5bcbdde63ab27096', '5664c511639700c88ad44724dac0d22f', 'd325e507642a8be49f6b921b9378cc6f', '90fa6ca33177482e908cf23c4c62671e', '312c1f0bdec49de9f17672d9bb819eef', '07a5560145f511eb764f6fe79357dd17', 'd591ac4b486e36a7633784530b95929b', '1d3a00f848fa1347d3a511e24329dc0a', '03b1edd1665ad1e96e61d0fa98acb62d', '1a90d11f5cd881ac1281a062da6a5854', 'da7c55880f470e6c47a14fc7c208dd28', '7b885b2328d8add80d4c124f653891de', 'e302317f97a4a7a1d0073d06e596b3b6', '370c9b900f57e0314c7fe3f35cc1e3e4', '8d2c976c155e4c58a407a6188a68d62c', 'd633c196bc63bdb4984e25eead92f9bf', '46574303426c84d8bce47d0b2fa1da59', 'a5d6d7bd487ea2412ce92730a177975f', 'b7df588e16e0e0b2a3b9b5fe594d421d', '78f5e19f50a2baadee2e4e5628a9e6a9', '709682bf41e33c5bbaa83348fd7ee511', '82b348444c882d68217bb003e16aca14', '2879fd6e6c0e484ea7a8148c5261bdbf', 'a5dd6f2c9cec67989db0f38a66994857', 'b86cd456039c33a9a47d9c8b30bdfcec', '33d0a0123a1d7d0ed374a80385f83541', '78dc7fd8326113fb5ad466c3c8153977', '68354b27485b40bd09cec730de364c4b', '0090937301ab25ed9e8d6bc008a9464d', '7608a3fc79a4812b61377fc331058008', 'c706b21d1609490d84a5d72eb0b26f80', 'c2e9892dfe4a2d84ce89528d09dbf42c', '3fa3a313b9f870a36c99b7e8f68298f8', '602e502d66d8b8c3680306b325010408', '096f2efaa4e4158396a71e4aa4d8e994', '8a8573e5837a5d9d6b5e99c4b2b41bd5', '6106fc978f864599a8b31d23ebb8ac03', 'd70794115ae075cdbc6dbefc9eaf57a2', '9c6cf0fc282bc4f2268905d6570f8865', '8938c40a0f29e251ad83452a2d89313e', '8bbc2eade35d915edcfa9b301825f085', '27c45f8487ce5f2aca1a644b5c116ddb', 'fa25074b3cdd9156a6ddd77d4bae9c1d', '38e8cc0793f0d897d09656e6ec74cf96', '88fe1cdff0324a43b276fc5a4f824e9f', '3f0c8d960374c8884359c7b243787e35', 'cdc1f67ad9398a5b1e4b66dad2254ce3', '253038c7d937db66e586730ca69ff66a', 'd8a48ee9a82ff57b4284a279ec5861da', 'f384fcb7bc2c30116470f2d15ce20e0a', 'e34daa89ca56c722beac563723a85854', '9595ce67e5d180883e8c6a0243564f15', '2e99bcb6515509caa2fbb144b72f1d53', '008d971e7cd365b5d92c0e032ac29df6', '892ee734bcde7a869befcec8944c3878', '74596e38f323e5c8158dfae96620eda6']
	# for inp in inputs:
	# 	hashes.append(knotHash(inp))

	hexed = []
	for h in hashes:
		hexed.append(bin(int(h, 16))[2:].zfill(128))

	used = 0
	for l in hexed:
		used += l.count("1")
	return used

#Function from Day 10 Part 2
def knotHash(n):
	asciiInput = []
	for ch in n:
		asciiInput.append(ord(ch))
	asciiInput = asciiInput + [17, 31, 73, 47, 23]

	t = []
	for i in range(256):
		t.append(i)

	skip = 0
	index = 0
	sixtyfour = 64
	while sixtyfour > 0:
		for i in asciiInput:
			if index + i >= len(t):
				reversal = t[index:] + t[:i-len(t[index:])]
			else :
				reversal = t[index:index+i]
			reversal.reverse()
			
			ind = 0
			tempreverse = index
			while ind < i:
				t[tempreverse] = reversal[ind]
				ind += 1
				tempreverse += 1
				if tempreverse == len(t):
					tempreverse = 0

			posforward = i + skip
			while posforward > 0:
				index += 1
				if index == len(t):
					index = 0
				posforward -= 1
			skip += 1
		sixtyfour -= 1
	
	retXOR = []
	retIndex = 16
	while retIndex <= 256:
		xor = 0
		for thing in t[retIndex-16:retIndex]:
			xor = xor ^ thing
		retXOR.append(xor)
		retIndex += 16

	returned = ""

	for element in retXOR:
		add = hex(element)[2:]
		if len(add) < 2:
			add = "0" + add
		returned = returned + add

	return returned

'''
--- Part Two ---

Now, all the defragmenter needs to know is the number of regions. A region is a group of used squares that are all adjacent, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.

In the example above, the following nine regions are visible, each marked with a distinct digit:

11.2.3..-->
.1.2.3.4   
....5.6.   
7.8.55.9   
.88.5...   
88..5..8   
.8...8..   
88.8.88.-->
|      |   
V      V   
Of particular interest is the region marked 8; while it does not appear contiguous in this small view, all of the squares marked 8 are connected when considering the whole 128x128 grid. In total, in this example, 1242 regions are present.

How many regions are present given your key string?

Your puzzle input was jzgqcdpd.

Your puzzle answer was 1212.
'''
def diskDefragmentationP2(n):
	inputs = []
	for i in range(128):
		inputs.append(n+"-"+str(i))

	hashes = ['7bd6e074b46be65cb4876aae96545d34', 'b53f5f98200ad3323d58fb9165a6c18b', 'da410b6eb19517bad150865916a933a5', 'd069a7ca568f8d473c5806d09882224d', '5d8e518f016a8b2f87f3298fcc093ce9', 'cbf7131a094822e7869fe68ae705c0e6', 'a0ffd078e72a1ca55b0e6c6240b0765e', '18263142dd187843a1a073157f53c43c', 'a389beb5a020bacbdfb2a7e0274bdc4a', 'd5234fd0d0b239a86e1318e5f38d492d', '24c7439f99e0a7f6574bbee521bd6ea2', 'c99873818c9bf2dcc5eb93e2ecd841b0', 'c1cb41bdf13af897c08386a0f31d7fa6', '82297b904fdbfab7040d93c3d22d053a', '350b013d3352968fc6f4a8e320ad5ad4', '77ddfc0a1cb7e37d36182f58e1b7fc9a', '0ca7c37641ca933b09e9891bbe70ec6d', '22af75be22ce3fb6ab4023826c56386b', 'a6477adc855f5956a2980cd65a50c6be', '5a6ab76aa7ee2e2b058c2f8a108bdfc9', 'd0ea8e3178f901a77350ecbc134f1c91', '5137793cc3fcb613b285d13bcdf55b07', 'c8042ea891f17c1937cdab7f09b57da0', '88bdff667431bab4f48e49bc2459dfca', '6072168cc9bfa8df4d50802880a4afb7', 'ed526f0de154c581c102be4c4c6591a5', '80fa45b4f7d89bedd65ef9a025808620', '380518bdb443582170dc4270224cb157', '55028011c2bb307314b19f5a1ce395f6', 'cc0f987cd0f8fe3ebb39175489770bfb', '72b4813165c1db1a4c469da76b843df1', 'd4604c2740a91db29af53fbddee51e51', '1a756b899355b2cb259f94a655ea6663', '5166858290345b19b795ef3a3743580d', '77dd6566f3ca0b93e7922290616b08cd', '05b256a648dc7d0bb94fb7b076e18142', '055af0f9d9a370c9e0dae8ac95423408', '362894f23c2f5992b79de4c09033dfd2', 'f09b7dec160d50442c43118110afd267', 'b82c3adfaf1932ff899fc6ff2969bcd9', '13fcf2a4f9e2efc6a158cc99ecb9b3c1', '5267e8b6a3e542dbb7dc42bf4b24e9a4', 'f20e1ca91c491308d73962785683efc9', 'dae96a9d71a80215e2a2097e832da132', '15fc31a9a64b719ac2463da6cf1117a1', '4f1e6b05af0026dbbf97ac2a394ad969', '27c7d592d6db1df695e85fcb15c56c14', 'a9c2ce40b85cf7f093cc42e2fa675733', 'dac51dabfa78a2b25b4875d1748adaa8', '8c992a2c2a41ed0305aef16432528d45', 'f77ab846a9a157e55dafca60d3cdd956', 'fa8588b29d29bc435d40a101e899ca08', '9eb4ef941c7501d55a6b14a29aa55703', '86a50cd2b86d3957373a53c41ddbe0fa', '1f94a471131d598881ab85d58ab426e3', '906381abd01558900b2cc10331b303b0', 'a6b84c384000f97d62bfea54341b2ac8', '58ba35cfd96686aea5ba8bb70e42b858', 'a7c3c19e7e2484c3702c812ae82e4453', '921465c6a697c1daab196294c5ffe190', '924b56d7e11bb60acf155de616464a65', '111cd1885243955c85b2d053235a7f3e', 'b0d6af9f24f2bd235cd137b96b226f3b', '29187adf2154f9f71bedeaeadc511c88', '668a576715132c6195047cf52fd5daaf', 'c2b7a70332c5793177bbf06a5d9e7c87', '965b0d91596a590c8b83df1ddab8f966', '9417368703f03b2604f9cf5784a7e47e', 'f2fd2dc7c7b7045970d6f92ef6b71de5', 'c103dcce9b765d805c868ccddcbe5a43', '888c0491709d9822114828517c0ae575', 'd23491cc1a10efb2443ea34b80f14c43', '580be6a8b2aff83d5bcbdde63ab27096', '5664c511639700c88ad44724dac0d22f', 'd325e507642a8be49f6b921b9378cc6f', '90fa6ca33177482e908cf23c4c62671e', '312c1f0bdec49de9f17672d9bb819eef', '07a5560145f511eb764f6fe79357dd17', 'd591ac4b486e36a7633784530b95929b', '1d3a00f848fa1347d3a511e24329dc0a', '03b1edd1665ad1e96e61d0fa98acb62d', '1a90d11f5cd881ac1281a062da6a5854', 'da7c55880f470e6c47a14fc7c208dd28', '7b885b2328d8add80d4c124f653891de', 'e302317f97a4a7a1d0073d06e596b3b6', '370c9b900f57e0314c7fe3f35cc1e3e4', '8d2c976c155e4c58a407a6188a68d62c', 'd633c196bc63bdb4984e25eead92f9bf', '46574303426c84d8bce47d0b2fa1da59', 'a5d6d7bd487ea2412ce92730a177975f', 'b7df588e16e0e0b2a3b9b5fe594d421d', '78f5e19f50a2baadee2e4e5628a9e6a9', '709682bf41e33c5bbaa83348fd7ee511', '82b348444c882d68217bb003e16aca14', '2879fd6e6c0e484ea7a8148c5261bdbf', 'a5dd6f2c9cec67989db0f38a66994857', 'b86cd456039c33a9a47d9c8b30bdfcec', '33d0a0123a1d7d0ed374a80385f83541', '78dc7fd8326113fb5ad466c3c8153977', '68354b27485b40bd09cec730de364c4b', '0090937301ab25ed9e8d6bc008a9464d', '7608a3fc79a4812b61377fc331058008', 'c706b21d1609490d84a5d72eb0b26f80', 'c2e9892dfe4a2d84ce89528d09dbf42c', '3fa3a313b9f870a36c99b7e8f68298f8', '602e502d66d8b8c3680306b325010408', '096f2efaa4e4158396a71e4aa4d8e994', '8a8573e5837a5d9d6b5e99c4b2b41bd5', '6106fc978f864599a8b31d23ebb8ac03', 'd70794115ae075cdbc6dbefc9eaf57a2', '9c6cf0fc282bc4f2268905d6570f8865', '8938c40a0f29e251ad83452a2d89313e', '8bbc2eade35d915edcfa9b301825f085', '27c45f8487ce5f2aca1a644b5c116ddb', 'fa25074b3cdd9156a6ddd77d4bae9c1d', '38e8cc0793f0d897d09656e6ec74cf96', '88fe1cdff0324a43b276fc5a4f824e9f', '3f0c8d960374c8884359c7b243787e35', 'cdc1f67ad9398a5b1e4b66dad2254ce3', '253038c7d937db66e586730ca69ff66a', 'd8a48ee9a82ff57b4284a279ec5861da', 'f384fcb7bc2c30116470f2d15ce20e0a', 'e34daa89ca56c722beac563723a85854', '9595ce67e5d180883e8c6a0243564f15', '2e99bcb6515509caa2fbb144b72f1d53', '008d971e7cd365b5d92c0e032ac29df6', '892ee734bcde7a869befcec8944c3878', '74596e38f323e5c8158dfae96620eda6']
	# for inp in inputs:
	# 	hashes.append(knotHash(inp))

	hexed = []
	for h in hashes:
		hexed.append(bin(int(h, 16))[2:].zfill(128))

	check = []
	for i in range(128):
		for j in range(128):
			if hexed[i][j] == "1":
				check.append((i, j))
	groups = 0
	while len(check) > 0:
		nextup = [check[0]]
		while len(nextup) > 0:
			current = nextup.pop()
			if current in check:
				check.remove(current)
				(i, j) = current
				nextup.append((i-1, j))
				nextup.append((i+1, j))
				nextup.append((i, j-1))
				nextup.append((i, j+1))
		groups += 1
	return groups

if __name__ == '__main__':
    print(diskDefragmentationP1("jzgqcdpd"))
    print(diskDefragmentationP2("jzgqcdpd"))