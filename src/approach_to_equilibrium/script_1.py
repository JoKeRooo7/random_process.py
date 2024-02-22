import random
import matplotlib.pyplot as plt

class Box:
    def __init__(self, n, n_on_left=None):
        self.n = n
        self.x = [0.5 * random.random() for _ in range(n)]
        self.y = [random.random() for _ in range(n)]
        self.n_left = n if n_on_left is None else n_on_left
        self.time = 0
        # graphic
        self.pause = 0.1
        self.x_min = 0
        self.x_max = 1
        self.picture = None
        self.yx = None
    
    def step(self):
        i = int(random.random() * self.n)
        if self.x[i] < 0.5:
            self.n_left -= 1
            self.x[i] = 0.5 * (1 + random.random())
            self.y[i] = random.random()
        else:
            self.n_left += 1
            self.x[i] = 0.5 * random.random()
            self.y[i] = random.random()
        self.time += 1

    def visual(self):
        if self.picture is None:
            self.picture, self.yx = plt.subplots()
            self.__draw_visual()
            plt.show(block=False)
        else:
            self.yx.clear()
            self.__draw_visual()
            plt.pause(self.pause)

    def __draw_visual(self):
        self.yx.axvline(x=0.5, color='black', linestyle='--')
        self.yx.scatter(self.x, self.y)
        self.yx.set_xlabel('x')
        self.yx.set_ylabel('y')
        self.yx.set_title('Partitioned box')
        self.yx.set_xlim(self.x_min, self.x_max)


class BoxApp:
    def __init__(self, n, n_on_left=None):
        self.box = Box(n, n_on_left)
        self.history_left_particles = []

    def draw_history_left_particles(self):
        plt.plot(range(1, len(self.history_left_particles) + 1), self.history_left_particles)  # Построение графика
        plt.xlabel('Итерации')
        plt.ylabel('Частицы слева')
        plt.title('Изменение количества частиц слева')
        plt.show()

        
    def do_step(self):
        self.box.step()
        self.history_left_particles.append(self.box.n_left)

    def reset(self):
        self.box = Box(64)

    def __check_unstable_equilibrium(self):
        return self.box.n_left == self.box.n // 2

    def __check_stable_equilibrium(self, stop_after_corresponding):
        size = len(self.history_left_particles)

        if size < stop_after_corresponding:
            return False

        min_value = self.box.n_left - 1
        max_value = self.box.n_left + 1
        for i in range(size - stop_after_corresponding, size - 1):
            if (self.history_left_particles[i] < min_value or 
                self.history_left_particles[i] > max_value):
                return False

        return True

    def __check_equilibrium(self, stop_after_corresponding):
        if (stop_after_corresponding == 1):
            if self.__check_unstable_equilibrium():
                return True
        else:
            return self.__check_stable_equilibrium(stop_after_corresponding)

    def main(self, stop_after_corresponding=3,step=1000000, visual=False):
        if stop_after_corresponding < 1 or step < 1:
            raise "bad arguments"
        
        for _ in range(step):
            self.do_step()
            if visual:
                self.box.visual()

            if self.__check_equilibrium(stop_after_corresponding):
                break

        plt.close()
            
        # self.draw_history_left_particles()


def create_box(size, stop_after_corresponding=3, visual=False):
    my_box = BoxApp(size)
    my_box.main(stop_after_corresponding=stop_after_corresponding, visual=visual)
    return my_box


def main():
    my_box_8 = create_box(400, 3)
    # my_box_16 = create_box(16)
    # my_box_64 = create_box(64)
    # my_box_400 = create_box(400)
    # my_box_800 = create_box(800)
    # my_box_3600 = create_box(3600)

    plt.plot(range(1, len(my_box_8.history_left_particles) + 1), my_box_8.history_left_particles, label='8 particles')
    # plt.plot(range(1, len(my_box_16.history_left_particles) + 1), my_box_16.history_left_particles, label='800 particles')
    # plt.plot(range(1, len(my_box_64.history_left_particles) + 1), my_box_64.history_left_particles, label='3600 particles')
    plt.xlabel('step - Количество шагов')
    plt.ylabel('n - количество частиц слева')
    plt.title('Эволюция частиц')
    plt.legend()
    print(len(my_box_8.history_left_particles))
    # print(len(my_box_8.history_left_particles),
    #       len(my_box_16.history_left_particles),
    #       len(my_box_64.history_left_particles))

    # Отображаем графики
    plt.show()
    # my_box_8.draw_history_left_particles()
    # my_box_16.draw_history_left_particles()


if __name__ == "__main__":
    main()
