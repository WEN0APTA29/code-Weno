meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
# print(word)

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("Kata yang anda ketik adalah: ", word)
    print("kata yang anda ketik adalah: ", meme_ditc.get(word))
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("kata tidak ada")
