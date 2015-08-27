import random

def diffie_hellman(mod, base, quiet=False):
    """
    Computes a diffie hellman shared secret
    """
    alice_secret = random.choice(range(1000))
    bob_secret = random.choice(range(1000))

    alice_computation = (base**alice_secret) % mod
    bob_computation = (base**bob_secret) % mod

    alice_shared = (bob_computation**alice_secret) % mod
    bob_shared = (alice_computation**bob_secret) % mod

    if not quiet:
        print("Diffie-Hellman! We're using mod {} and base {}".format(mod, base))
        print("Alice chooses {} for her secret".format(alice_secret))
        print("Bob chooses {} for his secret".format(bob_secret))
        print("Bob computes {}, Alice computes {}".format(alice_computation, bob_computation))
        if alice_shared == bob_shared:
            print("The shared secret is {}".format(alice_shared))
        else:
            print("They didn't agree, oops!")
            print("Alice: {}, Bob: {}".format(alice_shared, bob_shared))
    if alice_shared == bob_shared:
        return alice_shared
    else:
        return None

if __name__ == '__main__':
    diffie_hellman(53, 22)
