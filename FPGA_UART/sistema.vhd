library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;



entity sistema is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		rx_empty : in std_logic;
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
		rx_empty : in std_logic;
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		w_data: out std_logic_vector(8-1 downto 0)
	);
    end component;

begin
    
    detector_i: detector
		port map(
			clk_i 		=>  clk_i,
			rst_i       =>  rst_i,
			rx_empty   => rx_empty,
			r_data     => r_data,
			led_rgb_1 => led_rgb_1,
			led_rgb_2 => led_rgb_2,
			w_data     => w_data
		);	
		
        --w_data <= r_data;
        
end Behavioral;
