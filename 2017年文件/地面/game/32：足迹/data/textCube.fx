string description = "Basic Vertex Lighting with a Texture";

//------------------------------------

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;


texture diffuseTexture : Diffuse
<
	string ResourceName = "default_color.dds";
>;



//------------------------------------
struct vertexInput {
    float3 position				: POSITION;    
    float2 texCoordDiffuse		: TEXCOORD0;
    float4 data		: COLOR;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float2 texCoordDiffuse	: TEXCOORD0;
    float2 alpha	: TEXCOORD1;
};


//------------------------------------
vertexOutput VS_TransformAndTexture(vertexInput IN) 
{
    vertexOutput OUT = (vertexOutput)0;

    

    float4 Pos = float4(IN.position,1); 
    float2 Pos2 = Pos.xy;
    
    Pos.x = Pos2.x * cos(IN.data.z) + Pos2.y * sin(IN.data.z);
    Pos.y = Pos2.y * cos(IN.data.z)-Pos2.x * sin(IN.data.z);
    Pos.x +=IN.data.x;
    Pos.y +=IN.data.y;	
    
    Pos = mul(Pos,viewProjection);   

 
    OUT.hPosition  = Pos;
    OUT.texCoordDiffuse = IN.texCoordDiffuse;  
    OUT.alpha.x =  IN.data.w;
    return OUT;
}


//------------------------------------
sampler TextureSampler = sampler_state 
{
    texture = <diffuseTexture>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};


//-----------------------------------
float4 PS_Textured( vertexOutput IN): COLOR
{

float4 diffuseTexture = tex2D( TextureSampler,IN.texCoordDiffuse);
diffuseTexture.xyz = float3(0.93,0.82,0.61);
diffuseTexture.a = diffuseTexture.a*(IN.alpha.x);
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
	//outputPS.RGBColor = float4(al.r,al.r,al.r,al.r);
	return outputPS;
	
}


technique RenderSceneBlend
{
    

    pass P1
    {          
        
        PixelShader  = compile ps_3_0 RenderScenePS_Blend2();
    }
 
}

bool side;
float alpha;
PS_OUTPUT RenderScenePS_Alpha( VS_OUTPUT In ) 
{
	PS_OUTPUT outputPS;	
	float2 uv;
	if(side)
		uv = float2(1-In.TextureUV.x,In.TextureUV.y);
	else
		uv =In.TextureUV;
	float4 al =  tex2D(MeshTextureSampler_alpha,uv);
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

PS_OUTPUT RenderScenePS_Foot( VS_OUTPUT In ) 
{
	PS_OUTPUT outputPS;	
	float2 uv;
	if(side)
		uv = float2(1-In.TextureUV.x,In.TextureUV.y);
	else
		uv =In.TextureUV;
	
	float4 al =  tex2D(MeshTextureSampler_alpha, uv);
	al.a = al.a*alpha;
	outputPS.RGBColor =al;
	return outputPS;	
}

technique RenderSceneFoot
{
    

    pass P1
    {          
        
        PixelShader  = compile ps_3_0 RenderScenePS_Foot();
    }
 
}

