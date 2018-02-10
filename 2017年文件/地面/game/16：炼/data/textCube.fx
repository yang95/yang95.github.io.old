string description = "Basic Vertex Lighting with a Texture";

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;

texture t1 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t1s = sampler_state 
{
    texture = <t1>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t2 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t2s = sampler_state 
{
    texture = <t2>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t3 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t3s = sampler_state 
{
    texture = <t3>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t4 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t4s = sampler_state 
{
    texture = <t4>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};



texture t5 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t5s = sampler_state 
{
    texture = <t5>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t6 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t6s = sampler_state 
{
    texture = <t6>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};


//------------------------------------
struct vertexInput {
    float3 position				: POSITION;    
    float2 texCoordDiffuse		: TEXCOORD0;
    float4 data		: COLOR0;
	float4 color		: COLOR1;
	float4 c2		: COLOR2;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float2 texCoordDiffuse	: TEXCOORD0;
    float2 texID	: TEXCOORD1;
	float4 color		: COLOR;
};


//------------------------------------
vertexOutput VS_TransformAndTexture(vertexInput IN) 
{
    vertexOutput OUT = (vertexOutput)0;

    float4 Pos = float4(IN.position*IN.c2.x,1); 
    float2 Pos2 = Pos.xy;
    
    Pos.x = Pos2.x * cos(IN.data.z) + Pos2.y * sin(IN.data.z);
    Pos.y = Pos2.y * cos(IN.data.z)-Pos2.x * sin(IN.data.z);
    Pos.x +=IN.data.x;
    Pos.y +=IN.data.y;	
    
    Pos = mul(Pos,viewProjection);   

 
    OUT.hPosition  = Pos;
    OUT.texCoordDiffuse = IN.texCoordDiffuse;  
    OUT.texID.x =  IN.data.w;
	OUT.color = IN.color;
	
    return OUT;
}





//-----------------------------------
float4 PS_Textured( vertexOutput IN): COLOR
{

float4 diffuseTexture;
int index = IN.texID.x+1;
if(index==1) 
   diffuseTexture = tex2D(t1s,IN.texCoordDiffuse.xy );
else if(index==2) 
   diffuseTexture = tex2D(t2s,IN.texCoordDiffuse.xy );
else if(index==3) 
   diffuseTexture = tex2D(t3s,IN.texCoordDiffuse.xy );
else if(index==4) 
   diffuseTexture = tex2D(t4s,IN.texCoordDiffuse.xy );  
else if(index==5) 
   diffuseTexture = tex2D(t4s,IN.texCoordDiffuse.xy );   
else if(index==6) 
   diffuseTexture = tex2D(t4s,IN.texCoordDiffuse.xy );      

   diffuseTexture = diffuseTexture * IN.color; 
   
return diffuseTexture;

}


//-----------------------------------
technique textured
{
    pass p0 
    {		
		VertexShader = compile vs_3_0 VS_TransformAndTexture();
		PixelShader  = compile ps_3_0 PS_Textured();
    }
}



texture g_MeshTexture_bk;              // Color texture for mesh
texture g_MeshTexture_fg;              // Color texture for mesh
texture g_MeshTexture_alpha;           // Color texture for mesh

sampler MeshTextureSampler_bk = 
sampler_state
{
    Texture = <g_MeshTexture_bk>;
    MipFilter = LINEAR;
    MinFilter = LINEAR;
    MagFilter = LINEAR;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
};

sampler MeshTextureSampler_fg = 
sampler_state
{
    Texture = <g_MeshTexture_fg>;
    MipFilter = LINEAR;
    MinFilter = LINEAR;
    MagFilter = LINEAR;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    
};
sampler MeshTextureSampler_alpha = 
sampler_state
{
    Texture = <g_MeshTexture_alpha>;
    MipFilter = LINEAR;
    MinFilter = LINEAR;
    MagFilter = LINEAR;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    
};



struct VS_OUTPUT
{
    float2 TextureUV  : TEXCOORD0;  // vertex texture coords 
};



struct PS_OUTPUT
{
    float4 RGBColor : COLOR0;  // Pixel color    
};




PS_OUTPUT RenderScenePS_Blend2( VS_OUTPUT In ) 
{
	PS_OUTPUT outputPS;
	float4 FG =  tex2D(MeshTextureSampler_fg, In.TextureUV);
	float4 BG =  tex2D(MeshTextureSampler_bk, In.TextureUV);
	float4 al =  tex2D(MeshTextureSampler_alpha, In.TextureUV);
	
	
	outputPS.RGBColor =FG*(1-al.r)+BG*al.r;
	//outputPS.RGBColor = BG;
	return outputPS;
	
}


technique RenderSceneBlend
{
    

    pass P1
    {          
        
        PixelShader  = compile ps_3_0 RenderScenePS_Blend2();
    }
 
}


float alpha;
PS_OUTPUT RenderScenePS_Alpha( VS_OUTPUT In ) 
{
	PS_OUTPUT outputPS;	
	float4 al =  tex2D(MeshTextureSampler_alpha, In.TextureUV);
	al.r = al.r*alpha;
	outputPS.RGBColor =al;	
	return outputPS;	
}

technique RenderSceneAlpha
{
    

    pass P1
    {          
        
        PixelShader  = compile ps_3_0 RenderScenePS_Alpha();
    }
 
}
