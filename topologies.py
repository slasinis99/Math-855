from itertools import chain, combinations

def power_set(s) -> list:
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def discrete_topology(n: int):
    s = set(range(1, n+1))
    p_set = power_set(s)
    p_set = [set(e) for e in p_set]
    return power_set(p_set)

def is_valid_topology(s, t):
    t = [set(e) for e in t]
    if not set() in t:
        return False
    if not s in t:
        return False
    for U, V in combinations(t, 2):
        if not U & V in t:
            return False
    for subset in power_set(t):
        if not set().union(*subset) in t:
            return False
    return True

def all_topology_n_elements(n: int):
    s = set(range(1, n+1))
    dt = discrete_topology(n)
    all_t = []
    for candidate in dt:
        if is_valid_topology(s, candidate):
            all_t.append(candidate)
    return all_t

def complements_of_topology(X, t):
    comp = []
    for subset in t:
        comp.append(X - subset)
    return comp

def all_complements_n_elements(n: int):
    X = set(range(1, n+1))
    t_list = all_topology_n_elements(n)
    c_list = []
    for t in t_list:
        c_list.append(complements_of_topology(X, t))
    return c_list

# Latex conversion for 2.5
c_list = all_topology_n_elements(3)
print(f'Number of 3-element topologies = {len(c_list)}')
print(f'Here is the list of all collections of subsets of a 3-elements set which are collections of closed sets for some topology:')
d = {1:'a', 2:'b', 3:'c'}
for c in c_list:
    l = [set()]
    el = sorted(c, key=lambda x: len(x))
    el = el[1:len(el)]
    el.sort(key=lambda x: (len(x), next(iter(x))))
    l.extend(el)
    
    s = '&\\{'
    for e in l:
        if len(e) == 0:
            s += '\\emptyset, '
        else:
            s += ' \\{'
            for i in e:
                s += f'{d[i]},'
            s = s[0:len(s)-1]
            s += '\\}, '
    s = s[0:len(s)-2]
    s += '\\} \\\\'
    print(s)