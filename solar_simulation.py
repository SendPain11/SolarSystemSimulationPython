# This is Solar Simulation Program
import pygame
import math 
import random
pygame.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Simulation Solar System")

# Create Pallete Color Scheme
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255, 165, 0)
BROWN = (210, 180, 140)  # Warna lebih terang untuk Saturnus
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
VENUS_COLOR = (255, 220, 180)  # Warna khusus Venus

FONT = pygame.font.SysFont("Arial", 14)
TITLE_FONT = pygame.font.SysFont("Arial", 22, bold=True)
INFO_FONT = pygame.font.SysFont("Arial", 13)
HEADER_FONT = pygame.font.SysFont("Arial", 16, bold=True)

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 60 / AU  # Skala lebih kecil
    TIMESTEP = 3600*24

    def __init__(self, x, y, radius, color, mass, name="", description=""):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name
        self.description = description  # Deskripsi planet

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win, selected_planet=None):
        x = self.x * self.SCALE + (WIDTH - 350) / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # Gambar orbit
        if len(self.orbit) > 2:
            updated_points = []       
            for point in self.orbit:
                x_point, y_point = point
                x_point = x_point * self.SCALE + (WIDTH - 350) / 2
                y_point = y_point * self.SCALE + HEIGHT / 2
                updated_points.append((x_point, y_point))
            
            if len(updated_points) > 1:
                orbit_color = (min(255, self.color[0]+50), 
                              min(255, self.color[1]+50), 
                              min(255, self.color[2]+50), 100)
                pygame.draw.lines(win, orbit_color, False, updated_points, 1)

        # Gambar planet
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)
        
        # Gambar glow untuk matahari (lebih kecil)
        if self.sun:
            for i in range(2):
                glow_radius = self.radius + (i+1)*2
                pygame.draw.circle(win, YELLOW, (int(x), int(y)), glow_radius, 1)
        
        # Gambar nama planet
        if self.name and not self.sun:  # Jangan tampilkan nama untuk matahari di sini
            name_text = INFO_FONT.render(self.name, 1, WHITE)
            text_rect = name_text.get_rect(center=(int(x), int(y) - self.radius - 12))
            
            # Background untuk nama
            bg_rect = text_rect.inflate(8, 4)
            pygame.draw.rect(win, (0, 0, 0, 180), bg_rect, border_radius=3)
            pygame.draw.rect(win, self.color, bg_rect, 1, border_radius=3)
            
            win.blit(name_text, text_rect)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        
        if len(self.orbit) > 400:
            self.orbit = self.orbit[-400:]

def draw_sidebar(win, planets, selected_planet):
    # Gambar background sidebar
    sidebar_rect = pygame.Rect(WIDTH - 350, 0, 350, HEIGHT)
    pygame.draw.rect(win, (15, 15, 25), sidebar_rect)
    pygame.draw.rect(win, (40, 40, 60), sidebar_rect, 2)
    
    # Judul sidebar
    title = TITLE_FONT.render("INFORMASI TATA SURYA", 1, YELLOW)
    win.blit(title, (WIDTH - 330, 20))
    
    if selected_planet:
        # Header informasi planet yang dipilih
        header = HEADER_FONT.render(f"INFORMASI {selected_planet.name.upper()}", 1, selected_planet.color)
        win.blit(header, (WIDTH - 330, 60))
        
        info_y = 90
        
        # Gambar ikon planet kecil
        pygame.draw.circle(win, selected_planet.color, (WIDTH - 330 + 15, info_y + 10), 12)
        
        # Data planet dalam format yang lebih rapi
        info_sections = [
            ("DATA FISIK", [
                f"Massa: {selected_planet.mass:.2e} kg",
                f"Jarak dari Matahari:",
                f"  {selected_planet.distance_to_sun/Planet.AU:.2f} AU",
                f"  {selected_planet.distance_to_sun/1000:,.0f} km",
                f"Kecepatan orbit:",
                f"  {math.sqrt(selected_planet.x_vel**2 + selected_planet.y_vel**2)/1000:.2f} km/s"
            ]),
            
            ("POSISI DAN KECEPATAN", [
                f"Posisi X: {selected_planet.x/Planet.AU:.2f} AU",
                f"Posisi Y: {selected_planet.y/Planet.AU:.2f} AU",
                f"Kecepatan X: {selected_planet.x_vel/1000:.2f} km/s",
                f"Kecepatan Y: {selected_planet.y_vel/1000:.2f} km/s"
            ])
        ]
        
        for section_title, lines in info_sections:
            # Gambar header section
            section_y = info_y
            section_header = INFO_FONT.render(section_title, 1, YELLOW)
            win.blit(section_header, (WIDTH - 330, section_y))
            info_y += 25
            
            # Gambar garis pemisah
            pygame.draw.line(win, (60, 60, 80), 
                           (WIDTH - 330, info_y), 
                           (WIDTH - 50, info_y), 1)
            info_y += 10
            
            # Tampilkan setiap baris informasi
            for line in lines:
                text = INFO_FONT.render(line, 1, WHITE)
                win.blit(text, (WIDTH - 320, info_y))
                info_y += 20
            
            info_y += 10
        
        # Deskripsi planet jika ada
        if selected_planet.description:
            info_y += 10
            desc_header = INFO_FONT.render("DESKRIPSI:", 1, YELLOW)
            win.blit(desc_header, (WIDTH - 330, info_y))
            info_y += 25
            
            # Split deskripsi menjadi beberapa baris
            words = selected_planet.description.split()
            lines = []
            current_line = ""
            
            for word in words:
                test_line = current_line + " " + word if current_line else word
                if len(test_line) < 40:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            
            if current_line:
                lines.append(current_line)
            
            for line in lines:
                desc_text = INFO_FONT.render(line, 1, (200, 200, 200))
                win.blit(desc_text, (WIDTH - 320, info_y))
                info_y += 18
    
    # Bagian bawah: Daftar semua planet
    list_start_y = HEIGHT - 250 if selected_planet else HEIGHT - 400
    
    # Background untuk daftar planet
    list_bg = pygame.Rect(WIDTH - 340, list_start_y - 10, 330, 250)
    pygame.draw.rect(win, (25, 25, 35), list_bg, border_radius=5)
    pygame.draw.rect(win, (50, 50, 70), list_bg, 1, border_radius=5)
    
    list_header = HEADER_FONT.render("DAFTAR PLANET", 1, YELLOW)
    win.blit(list_header, (WIDTH - 330, list_start_y))
    list_start_y += 30
    
    # Gambar daftar planet
    for planet in planets:
        # Buat baris dengan background hover effect jika dipilih
        if planet == selected_planet:
            row_bg = pygame.Rect(WIDTH - 335, list_start_y - 5, 320, 25)
            pygame.draw.rect(win, (40, 40, 60), row_bg, border_radius=3)
            pygame.draw.rect(win, planet.color, row_bg, 1, border_radius=3)
        
        # Ikon planet kecil
        pygame.draw.circle(win, planet.color, (WIDTH - 320, list_start_y + 10), 6)
        
        # Nama planet
        planet_text = INFO_FONT.render(planet.name, 1, planet.color if planet != selected_planet else WHITE)
        win.blit(planet_text, (WIDTH - 300, list_start_y))
        
        # Jarak saat ini
        if not planet.sun:
            distance_au = planet.distance_to_sun/Planet.AU
            distance_text = INFO_FONT.render(f"{distance_au:5.2f} AU", 1, (180, 180, 180))
        else:
            distance_text = INFO_FONT.render("Tengah", 1, (180, 180, 180))
        
        win.blit(distance_text, (WIDTH - 180, list_start_y))
        
        list_start_y += 30
    
    # Petunjuk kontrol
    controls_y = HEIGHT - 100
    controls_bg = pygame.Rect(WIDTH - 340, controls_y - 10, 330, 90)
    pygame.draw.rect(win, (25, 25, 35), controls_bg, border_radius=5)
    pygame.draw.rect(win, (60, 60, 80), controls_bg, 1, border_radius=5)
    
    controls_title = INFO_FONT.render("KONTROL:", 1, GREEN)
    win.blit(controls_title, (WIDTH - 330, controls_y))
    controls_y += 25
    
    controls = [
        "Klik planet: Pilih informasi",
        "R: Reset pilihan  +/-: Zoom",
        "P: Pause/Resume  ESC: Keluar"
    ]
    
    for control in controls:
        control_text = INFO_FONT.render(control, 1, (180, 180, 180))
        win.blit(control_text, (WIDTH - 320, controls_y))
        controls_y += 20

def get_planet_at_pos(mouse_pos, planets):
    mouse_x, mouse_y = mouse_pos
    for planet in planets:
        planet_x = planet.x * planet.SCALE + (WIDTH - 350) / 2
        planet_y = planet.y * planet.SCALE + HEIGHT / 2
        
        distance = math.sqrt((mouse_x - planet_x)**2 + (mouse_y - planet_y)**2)
        if distance <= planet.radius + 15:  # Area klik lebih besar
            return planet
    return None

def main():
    run = True 
    paused = False
    clock = pygame.time.Clock()
    
    # Inisialisasi planet dengan deskripsi
    sun = Planet(0, 0, 20, YELLOW, 1.98892 * 10**30, "Matahari", 
                "Bintang pusat tata surya kita. Menyediakan energi untuk semua kehidupan di Bumi.")
    sun.sun = True
    
    mercury = Planet(0.387 * Planet.AU, 0, 5, DARK_GREY, 3.30 * 10**23, "Merkurius",
                    "Planet terkecil dan terdekat dengan Matahari. Suhu ekstrem antara siang dan malam.")
    mercury.y_vel = -47.4 * 1000
    
    venus = Planet(0.723 * Planet.AU, 0, 9, VENUS_COLOR, 4.8685 * 10**24, "Venus",
                  "Planet terpanas dengan atmosfer tebal karbon dioksida. Sering disebut 'kembaran Bumi'.")
    venus.y_vel = -35.02 * 1000
    
    earth = Planet(-1 * Planet.AU, 0, 10, BLUE, 5.9742 * 10**24, "Bumi",
                  "Planet ketiga dari Matahari. Satu-satunya planet yang diketahui memiliki kehidupan.")
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 7, RED, 6.39 * 10**23, "Mars",
                 "Planet merah dengan gunung tertinggi di tata surya. Memiliki dua bulan kecil.")
    mars.y_vel = 24.077 * 1000
    
    jupiter = Planet(5.203 * Planet.AU, 0, 22, ORANGE, 1.898 * 10**27, "Jupiter",
                    "Planet terbesar di tata surya. Memiliki 79 bulan dan sistem cincin samar.")
    jupiter.y_vel = 13.07 * 1000
    
    saturn = Planet(9.537 * Planet.AU, 0, 19, BROWN, 5.683 * 10**26, "Saturnus",
                   "Dikenal dengan cincinnya yang spektakuler. Planet kedua terbesar setelah Jupiter.")
    saturn.y_vel = 9.69 * 1000
    
    uranus = Planet(19.191 * Planet.AU, 0, 15, CYAN, 8.681 * 10**25, "Uranus",
                   "Planet es raksasa dengan rotasi miring 98 derajat. Berwarna biru-hijau.")
    uranus.y_vel = 6.81 * 1000
    
    neptune = Planet(30.07 * Planet.AU, 0, 15, PURPLE, 1.024 * 10**26, "Neptunus",
                    "Planet terjauh dari Matahari. Memiliki angin terkuat di tata surya.")
    neptune.y_vel = 5.43 * 1000
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    
    selected_planet = earth  # Default pilih Bumi
    
    while run:
        clock.tick(60)
        WIN.fill((10, 10, 20))  # Dark blue untuk space
        
        # Gambar latar bintang
        for _ in range(150):
            x = random.randint(0, WIDTH - 350)
            y = random.randint(0, HEIGHT)
            brightness = random.randint(100, 255)
            size = random.choice([1, 1, 1, 2])  # Kebanyakan bintang kecil
            pygame.draw.circle(WIN, (brightness, brightness, brightness), (x, y), size)
        
        # Gambar beberapa bintang terang (lebih besar)
        for _ in range(10):
            x = random.randint(0, WIDTH - 350)
            y = random.randint(0, HEIGHT)
            pygame.draw.circle(WIN, WHITE, (x, y), 3)
        
        # Tangani event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_r:
                    selected_planet = None
                elif event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    Planet.SCALE *= 1.1
                elif event.key == pygame.K_MINUS:
                    Planet.SCALE *= 0.9
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Klik kiri
                    clicked_planet = get_planet_at_pos(event.pos, planets)
                    if clicked_planet:
                        selected_planet = clicked_planet
        
        # Update posisi planet jika tidak pause
        if not paused:
            for planet in planets:
                planet.update_position(planets)
        
        # Gambar semua planet
        for planet in planets:
            planet.draw(WIN, selected_planet)
        
        # Gambar sidebar informasi
        draw_sidebar(WIN, planets, selected_planet)
        
        # Gambar judul utama
        title = TITLE_FONT.render("SIMULASI TATA SURYA INTERAKTIF", 1, YELLOW)
        WIN.blit(title, (20, 20))
        
        # Status simulasi
        status = "PAUSED" if paused else "BERJALAN"
        status_color = RED if paused else GREEN
        status_text = INFO_FONT.render(f"Status: {status}", 1, status_color)
        WIN.blit(status_text, (20, 55))
        
        # Info planet yang dipilih
        if selected_planet:
            selected_info = INFO_FONT.render(f"Planet aktif: {selected_planet.name}", 1, selected_planet.color)
            WIN.blit(selected_info, (20, 80))
        
        # Informasi skala
        scale_factor = Planet.SCALE / (60 / Planet.AU)
        scale_info = INFO_FONT.render(f"Skala: 1 AU = {int(60*scale_factor)} pixels", 1, (150, 150, 150))
        WIN.blit(scale_info, (20, HEIGHT - 50))
        
        # Petunjuk
        hint = INFO_FONT.render("Klik pada planet untuk melihat informasi detailnya", 1, (200, 200, 100))
        WIN.blit(hint, (20, HEIGHT - 30))
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()