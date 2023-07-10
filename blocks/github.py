from prefect.filesystems import GitHub

block = GitHub(
    repository=f"https://github.com/m-tok/prefect-deploy.git",
    reference="main",
    access_token="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",
)

block_name = "my-git-repo"
block_id = block.save(block_name, overwrite=True)
print(f"Created block '{block_name}' with ID '{block_id}'")