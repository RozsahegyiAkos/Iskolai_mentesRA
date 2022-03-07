yes = ("Igen")
no = ("Nem")

henrik = str(input("Jön Henrik kosarazni? "))
hanna = str(input("Jön Hanna kosarazni? "))

if henrik and hanna == yes:
    print("Mindketten jönnek kosarazni.")
elif henrik and hanna == no:
    print("Egyik sem megy kosarazni.")