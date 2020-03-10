library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity detector is
	port(
		clk_i: in std_logic;
        	rst_i: in std_logic;
		r_data: in std_logic_vector(8-1 downto 0);
		r_disponible : in std_logic;
		led_rgb_1  : out std_logic_vector(3-1 downto 0);
		led_rgb_2  : out std_logic_vector(3-1 downto 0);
		paquete: out std_logic_vector(21-1 downto 0);
		procesar : in std_logic;
		procesado : out std_logic;
		N : in integer;
		N_1 : out integer;
		N_2 : out integer;
		wr_uart : out std_logic;
		w_data: out std_logic_vector(8-1 downto 0)
	);
end detector;

architecture Behavioral of detector is
    
    type estados_t is (inicio,lectura,final,error);
    signal estado, estado_siguiente : estados_t; 
  
    signal data_in :  std_logic_vector(8-1 downto 0);
    
    --signal data_ok: std_logic;
    
    --signal r_aux: std_logic;
    
    shared variable contador : integer range 0 to 30 := 0;
    signal ticks : integer range 0 to 407 := 0;
    
    signal paquete_aux : std_logic_vector(21-1 downto 0);
   -- signal paquete_ready : std_logic;
    
    signal nuevo : std_logic;
    signal largo_ok : std_logic;
    signal tags_ok : std_logic;
    signal tags_izq : std_logic;
    signal tags_der : std_logic;
    
    constant tag_inicial : std_logic_vector(8-1 downto 0) := "00111100"; -- r_data = '<'
    constant tag_final : std_logic_vector(8-1 downto 0) := "00111110"; -- r_data = '>'
    constant char_0 : std_logic_vector(8-1 downto 0) := "00110000"; -- r_data = '0'
    constant char_1 : std_logic_vector(8-1 downto 0) := "00110001"; -- r_data = '1'
    

begin
    
    cambio_estados : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                estado <= inicio;
            else
            if procesar = '1' then
                estado <= inicio;
            else
                estado <= estado_siguiente; 
            end if;
                      
            end if;
        end if;
    end process;
   
   incrementar_contador : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                contador := 0; 
            else
                if r_disponible = '1' then
                    if estado = lectura then
                        if contador < 23 then 
                            contador := contador + 1;
                        end if;
                    end if;
                end if;  
                if contador > 21 and contador < 23 then 
                     contador := contador + 1;
                end if;   
                if estado = final or estado = error then
                    contador := 0;
                end if; 
            end if;
        end if;
    end process;
    
   empaquetado : process(clk_i) 
   begin 
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                paquete_aux <= (others => '0');
                nuevo <= '0';
            else
                if estado = lectura then
                    if r_disponible = '1' then
                        if contador < 22 then
                            if r_data = char_0 then
                                paquete_aux(21-contador) <= '0';
                            end if;
                            if r_data = char_1 then
                                paquete_aux(21-contador) <= '1';
                            end if;
                        end if;
                        nuevo <= '1';
                    else        
                        nuevo <= '0';
                    end if;
                end if;
            end if;
        end if;
    end process;    
   
     estados : process(clk_i,estado)      
     begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then          
                estado_siguiente <= inicio;
                tags_izq <= '0'; 
                tags_der <= '0';
            else
            
                estado_siguiente <= estado;   
                -- LED4 = RGB2 | LED5 => RGB1
                -- BGR -> 001 = R | 010 = G | 100 = B
                case(estado) is                  
                            
                  when inicio =>            
                    --led_rgb_1 <= "100";   -- azul LD5
                    tags_izq <= '0'; 
                    if r_data = tag_inicial then -- r_data = '<'
                        tags_izq <= '1';
                        tags_der <= '0';
                        estado_siguiente <= lectura;                    
                    end if;               
                  when lectura => 
                    if contador = 23 then -- 21 (asi entran 21)
                        if r_data = tag_final then --  r_data = '>'
                            tags_der <= '1';               
                            estado_siguiente <= final;
                        else 
                            tags_der <= '0';    
                            estado_siguiente <= error;                       
                        end if;                      
                    else
                        tags_der <= '0';
                        --led_rgb_1 <= "101"; -- azul
                        --led_rgb_2 <= "100"; -- azul
                    end if; 
                  when final =>  
                    --led_rgb_1 <= "111"; -- blanco   
                    --led_rgb_2 <= "010"; -- verde
--                    if r_data = tag_inicial then -- r_data = '<'
--                        tags_izq <= '1';
--                        estado_siguiente <= lectura;                    
--                    end if; 
                       if procesar = '1' then
                            tags_izq <= '0'; 
                            estado_siguiente <= inicio;
                       end if;          
                  when error => 
                    --led_rgb_1 <= "111"; -- blanco        
                    --led_rgb_2 <= "001"; -- rojo
                    tags_izq <= '0';
                    tags_der <= '0';
                    
                    --if r_data = tag_inicial then -- r_data = '<'
                    --    tags_izq <= '1';
                        estado_siguiente <= inicio;                    
                    --end if;                
                  when others => null;
                end case;
             end if;
          end if;
      end process;
    
    lector_datos : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                data_in <= (others => '0'); 
            else  
                if r_disponible = '1' and r_data /= "00000000" then
                    data_in <= r_data; 
                end if;
            end if;
        end if;
    end process;
    
    paquete_listo : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                procesado <= '0';  
            else  
                if estado = final then          
                    procesado <= largo_ok and tags_ok;                                 
                else
                    procesado <= '0';   
                end if;
            end if;
        end if;
    end process;
    
    analizar_tags : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                tags_ok <= '0'; 
                led_rgb_1 <= "001"; -- rojo
            else  
                tags_ok <= tags_izq and tags_der;

                if tags_ok = '1' then
                    led_rgb_1 <= "010"; -- verde
                else
                    led_rgb_1 <= "001"; -- rojo
                end if;
                
                if estado = lectura then
                    led_rgb_1 <= "001"; -- rojo
                end if;
            end if;
        end if;
    end process;
    
    analizar_largo : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                largo_ok <= '0'; 
                led_rgb_2 <= "001"; -- rojo 
            else  
                if N = 23 then
                    largo_ok <= '1'; 
                    led_rgb_2 <= "010"; -- verde 
                    N_1 <= N;
                else
                    largo_ok <= '0';
                    led_rgb_2 <= "001"; -- rojo  
                    N_1 <= 0;  
                end if;
                
                if estado = lectura then
                    led_rgb_2 <= "001"; -- rojo
                end if;
                
            end if;
        end if;
    end process;
    
    paquete_valido : process(clk_i)
    begin
        if (clk_i = '1' and clk_i'event) then
            if rst_i = '1' then
                paquete <= (others => '0'); 
            else  
                       
                if estado = final and largo_ok = '1' and tags_ok = '1' then
                    paquete <= paquete_aux;
                end if;
                          
            end if;
        end if;
    end process;
    
    
    w_data <= r_data;
    wr_uart <= r_disponible;
    
    --w_data <= data_in;    -- Agrega 0 y rompe todo

       
end Behavioral;