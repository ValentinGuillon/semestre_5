let param = {
    longueur : 10,
};
let gui = new dat.GUI();
gui.add(param, 'longueur').min(10).max(100).step(1);
