from prefect.filesystems import LocalFileSystem
from prefect.infrastructure import Process

my_storage_block = LocalFileSystem(
    basepath="/Users/Menekse.Tok/first"
)
my_storage_block.save(
    name="demo",
    overwrite=True
)

my_process_infra = Process(working_dir="/Users/Menekse.Tok/work")
my_process_infra.save(
    name="process-infra",
    overwrite=True
)