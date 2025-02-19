-- Sistema.vhdl : Achivo VHDL generado automaticamente

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

	entity sistema is
		port(
			clk_i: in std_logic;		
			r_data: in std_logic_vector(8-1 downto 0);
			r_disponible : in std_logic;
			leer : out std_logic;
			escribir : out std_logic;
			switch1 : in std_logic;
			switch2 : in std_logic;
			reset_uart : out std_logic;
			N : in integer;
			leds : out std_logic_vector(4-1 downto 0);
			led_rgb_1  : out std_logic_vector(3-1 downto 0);
			led_rgb_2  : out std_logic_vector(3-1 downto 0);
			w_data: out std_logic_vector(8-1 downto 0);
			rst_i: in std_logic
		);
	end sistema;

architecture Behavioral of sistema is

    component detector is
		port(
			clk_i: in std_logic;      
			r_data: in std_logic_vector(8-1 downto 0);
			r_disponible : in std_logic;
			led_rgb_1  : out std_logic_vector(3-1 downto 0);
			led_rgb_2  : out std_logic_vector(3-1 downto 0);
			paquete: out std_logic_vector(21-1 downto 0);
			procesar : in std_logic;
			procesado : out std_logic;
			N : in integer;
			wr_uart : out std_logic;
			w_data: out std_logic_vector(8-1 downto 0);
			rst_i: in std_logic
		);
    end component;

    component enclavamiento is
		port(
			Clock: in std_logic;		
			procesar : in std_logic;
			procesado :  out std_logic;
			Paquete_i: in std_logic_vector(21-1 downto 0);
			Paquete_o: out std_logic_vector(15-1 downto 0);
			Reset: in std_logic
		);
    end component;
        
    component conector_test is
	port(
		clk_i: in std_logic;      
        switch : in std_logic;
        leds : out std_logic_vector(2-1 downto 0);
		wr_uart_1 : in std_logic;
        wr_uart_2 : in std_logic;
        wr_uart_3 : out std_logic;      
        w_data_1: in std_logic_vector(8-1 downto 0);
        w_data_2: in std_logic_vector(8-1 downto 0);
        w_data_3: out std_logic_vector(8-1 downto 0);
		rst_i: in std_logic
	);
    end component;
    
    component registro is
		port(
			clk_i: in std_logic;			
			procesar : in std_logic;
			procesado : out std_logic;
			paquete_i: in std_logic_vector(15-1 downto 0);
			w_data: out std_logic_vector(8-1 downto 0);
			wr_uart : out std_logic;
			rst_i: in std_logic
		);
    end component;
    
    signal paquete_i : std_logic_vector(21-1 downto 0);
    signal paquete_o : std_logic_vector(15-1 downto 0);
       
    signal w_data_1,w_data_2,w_data_3 : std_logic_vector(8-1 downto 0);
    signal wr_uart_1_s,wr_uart_2_s : std_logic;
    signal pro_enc_reg,pro_det_enc,pro_reg_det : std_logic;
    
begin
    
    detector_i: detector
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			r_data     => r_data,
			r_disponible => r_disponible,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			N        => N,
		    wr_uart     => wr_uart_1_s,
		    procesar => pro_reg_det,
			procesado => pro_det_enc,
			paquete  => paquete_i,
			w_data     => w_data_1
		);	
	
	enclavamiento_i: enclavamiento
		port map(
			Clock 		=>  clk_i,
			Reset       =>  rst_i,
			procesar  => pro_det_enc,
			procesado => pro_enc_reg,
			Paquete_i     => paquete_i,
			Paquete_o     => paquete_o
		);	
		
	registro_i: registro
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			procesar  => pro_enc_reg,
			procesado => pro_reg_det,
			paquete_i   => paquete_o,
			w_data     => w_data_2,
			wr_uart => wr_uart_2_s
		);
			
	conector_test_i: conector_test
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			switch      => switch1,
			wr_uart_1 => wr_uart_1_s,
			wr_uart_2 => wr_uart_2_s,
			wr_uart_3      => escribir,
			w_data_1     => w_data_1,
			w_data_2     => w_data_2,
			w_data_3     => w_data_3
		);
		
		w_data <= w_data_3;

        
        process(clk_i)
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
    
--        paquete_o(0) <= paquete_i(14);
--        paquete_o(1) <= paquete_i(13);
--        paquete_o(2) <= paquete_i(12);
--        paquete_o(3) <= paquete_i(11);
--        paquete_o(4) <= paquete_i(10);
--        paquete_o(5) <= paquete_i(9);
--        paquete_o(6) <= paquete_i(8);
--        paquete_o(7) <= paquete_i(7);
--        paquete_o(8) <= paquete_i(6);
--        paquete_o(9) <= paquete_i(5);
--        paquete_o(10) <= paquete_i(4);
--        paquete_o(11) <= paquete_i(3);
--        paquete_o(12) <= paquete_i(2);
--        paquete_o(13) <= paquete_i(1);
--        paquete_o(14) <= paquete_i(0);
        
end Behavioral;