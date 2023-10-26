import modal

stub = modal.Stub("get-started-cube")


@stub.function()
def cube(x):
    print("This code is running on a remote worker!")
    return x**3


@stub.local_entrypoint()
def main():
    print("the cube of 68 is", cube.remote(68))
