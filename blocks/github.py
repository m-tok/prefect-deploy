from prefect.filesystems import GitHub

block = GitHub(
    repository=f"https://github.com/m-tok/prefect-deploy.git",
    reference="main",
    access_token="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",
)

block_name = "my-git-repo"
block_id = block.save(block_name, overwrite=True)
print(f"Created block '{block_name}' with ID '{block_id}'")