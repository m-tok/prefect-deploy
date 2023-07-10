from prefect.filesystems import GitHub

block = GitHub(
    repository=f"https://github.com/m-tok/prefect-deploy.git",
    reference="main",
    access_token="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",
)

block_name = "my-git-repo"
block_id = block.save(block_name, overwrite=True)
print(f"Created block '{block_name}' with ID '{block_id}'")