library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity sistema is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		switch : in std_logic;
		btn : in std_logic;
		leds : out std_logic_vector(2-1 downto 0);
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		w_data: out std_logic_vector(8-1 downto 0)
	);
end sistema;

architecture Behavioral of sistema is

    component detector is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);	
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		paquete: out std_logic_vector(21-1 downto 0);
		paquete_ok : out std_logic;
		w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;

    component enclavamiento is
	port(
		Clock: in std_logic;
        Reset: in std_logic;
        paquete_ok : in std_logic;
        Paquete_i: in std_logic_vector(21-1 downto 0);
        Paquete_o: out std_logic_vector(15-1 downto 0)
	);
    end component;
    
    component fifo_enclavamiento is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_ok : in std_logic;
        paquete_i: in std_logic_vector(15-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;
    
    component retardador is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_ok : in std_logic;
        r_data: in std_logic_vector(8-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;
    
    component conector_test is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        switch : in std_logic;
        leds : out std_logic_vector(2-1 downto 0);
        w_data_1: in std_logic_vector(8-1 downto 0);
        w_data_2: in std_logic_vector(8-1 downto 0);
        w_data_3: out std_logic_vector(8-1 downto 0)
	);
    end component;
    
    component registro is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_ok : in std_logic;
        paquete_i: in std_logic_vector(15-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;
    
    signal paquete_i : std_logic_vector(21-1 downto 0);
    signal paquete_o : std_logic_vector(15-1 downto 0);
    signal prueba : std_logic_vector(15-1 downto 0);
    
    signal w_data_1,w_data_2,w_data_3,w_data_aux : std_logic_vector(8-1 downto 0);
    signal paquete_ok_s : std_logic;
begin
    
    detector_i: detector
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			r_data     => r_data,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			paquete_ok => paquete_ok_s,
			paquete  => paquete_i,
			w_data     => w_data_1
		);	
	
	enclavamiento_i: enclavamiento
		port map(
			Clock 		=>  clk_i,
			Reset       =>  rst_i,
			paquete_ok  => paquete_ok_s,
			Paquete_i     => paquete_i,
			Paquete_o     => paquete_o
		);	
	
	   fifo_enclavamiento_i: fifo_enclavamiento
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			paquete_ok  => paquete_ok_s,
			paquete_i   => paquete_o,
			--paquete_i   => prueba,
			w_data     => w_data_aux
		);	
		
		registro_i: registro
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			paquete_ok  => paquete_ok_s,
			paquete_i   => paquete_o,
			--paquete_i   => prueba,
			w_data     => w_data_2
		);
		
		retardador_i: retardador
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			paquete_ok  => paquete_ok_s,
			r_data   => w_data_aux,
			--r_data   => prueba,
			w_data     => open
		);	
		
		conector_test_i: conector_test
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			switch      => switch,
			leds       => leds,
			w_data_1     => w_data_1,
			w_data_2     => w_data_2,
			w_data_3     => w_data_3
		);
		
		w_data <= w_data_3;
		--prueba <= "0011001" & btn;
		prueba <= "10101010101010" & btn;	
        --w_data <= r_data;
        
end Behavioral;