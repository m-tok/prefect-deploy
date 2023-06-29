from prefect.filesystems import LocalFileSystem

my_storage_block = LocalFileSystem(
    basepath="/Users/Menekse.Tok/first"
)
my_storage_block.save(
    name="demo",
    overwrite=True
)

