class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity # Capacité totale
        self.items = [] # Liste d'items disponible
        self.selected_items = [] # Liste des items selectionnés

    def add_item(self, weight, value):
        self.items.append((weight, value))

    def solve(self):
        n = len(self.items)
        dp = [[0] * (self.capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(self.capacity + 1):
                item_weight, item_value = self.items[i - 1]
                if item_weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
                else:
                    dp[i][w] = dp[i - 1][w]

        max_value = dp[n][self.capacity]
        self.selected_items = []
        w = self.capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                self.selected_items.append(self.items[i - 1])
                w -= self.items[i - 1][0]

        return max_value

    def get_selected_items(self):
        return self.selected_items
