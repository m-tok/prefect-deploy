from prefect.filesystems import GitHub

block = GitHub(
    repository=f"https://github.com/organization/repo.git",
    reference="main",
    access_token="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",
)

block_name = "my-git-repo"
block_id = block.save(block_name, overwrite=True)
print(f"Created block '{block_name}' with ID '{block_id}'")