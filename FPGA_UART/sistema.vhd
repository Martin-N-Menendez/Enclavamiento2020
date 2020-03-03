library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity sistema is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		r_disponible : in std_logic;
		leer : out std_logic;
		escribir : out std_logic;
		switch1 : in std_logic;
		switch2 : in std_logic;
		reset_uart : out std_logic;
		N : in integer;
		--leds : out std_logic_vector(2-1 downto 0);
		leds : out std_logic_vector(4-1 downto 0);
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
		r_disponible : in std_logic;
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		paquete: out std_logic_vector(21-1 downto 0);
		paquete_ok : out std_logic;
		N : in integer;
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
        
    component conector_test is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        switch : in std_logic;
        leds : out std_logic_vector(2-1 downto 0);
        wr_uart : out std_logic;
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
    signal paquete_ok_s,escribir_s : std_logic;
begin
    
    detector_i: detector
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			r_data     => r_data,
			r_disponible => r_disponible,
			--leer       =>   leer,
			--escribir   => escribir_s,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			N        => N,
			--reset_uart => reset_uart,
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
		
		registro_i: registro
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			paquete_ok  => paquete_ok_s,
			paquete_i   => paquete_o,
			--paquete_i   => prueba,
			w_data     => w_data_2
			--w_data     => open
		);
		

		
		conector_test_i: conector_test
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			switch      => switch1,
			--escribir_2 => escribir_s,
			--escribir_3 => escribir,
			--N          => N,
			--leds(0)       => leds(0),
			--leds(1)       => leds(1),
			wr_uart      => escribir,
			w_data_1     => w_data_1,
			w_data_2     => w_data_2,
			w_data_3     => w_data_3
		);
		
		w_data <= w_data_3;
		--prueba <= "0011001" & btn;
		--prueba <= "101010101010101";	
        --w_data <= r_data;
        
        process(clk_i)
        --variable contador : integer range 0 to 125e6 := 0;
        begin
            if (clk_i = '1' and clk_i'event) then
                
                if switch2 = '1' then  
                    leds <= std_logic_vector(to_unsigned(N,4));                
                else
                    leds(3) <= paquete_i(3);
                    leds(2) <= paquete_i(2); 
                    leds(1) <= paquete_i(1); 
                    leds(0) <= paquete_i(0);  
                end if;
            end if;
        end process;  
    
        process(clk_i)
        variable contador: integer := 0;
            begin
                if (clk_i = '1' and clk_i'event) then
                    if rst_i = '1' then          
                        reset_uart <= '0'; 
                    else 
                        contador := contador + 1;
                      
                        if contador = 10*125E6 then    -- Cuento 5 mseg
                            contador := 0;
                            reset_uart <= '1'; 
                        else
                            reset_uart <= '0'; 
                        end if;

                    end if;
                end if;
  
            end process;
    
        
end Behavioral;