library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity fifo_enclavamiento is
	port(
		clk_i: in std_logic;
        rst_i: in std_logic;
        paquete_i: in std_logic_vector(17-1 downto 0);
        w_data: out std_logic_vector(8-1 downto 0)
	);
    end entity;

architecture Behavioral of fifo_enclavamiento is
    
    type estados_t is (espera,inicio,lectura,final,error);
    signal estado, estado_siguiente : estados_t; 
  
    signal char_data : std_logic_vector(8-1 downto 0);
    
    signal contador: std_logic_vector(3 downto 0);
    
begin
    
    
    
    process(clk_i)
    begin
        if rising_edge(clk_i) then
            if rst_i = '1' then
                char_data <= "00000000";
                contador <= (others => '0');
            else
                contador <= std_logic_vector(unsigned(contador) + 1);
                
                if paquete_i(to_integer(unsigned(contador))) = '0' then                 
                    char_data <= "00110000";
                end if;
                if paquete_i(to_integer(unsigned(contador))) = '1' then                 
                    char_data <= "00110001";
                end if;
                
            end if;
        end if;
    end process;
    
    --char_data <= r_data;
    
--   w_data(0) <= paquete_i(0);  
--   w_data(1) <= paquete_i(1); 
--   w_data(2) <= paquete_i(2); 
--   w_data(3) <= paquete_i(3); 
--   w_data(4) <= paquete_i(4); 
--   w_data(5) <= paquete_i(5); 
--   w_data(6) <= paquete_i(6); 
--   w_data(7) <= paquete_i(7);     

    --w_data <= "01100001";
      w_data <= char_data;
        
end Behavioral;
