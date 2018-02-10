string description = "Basic Vertex Lighting with a Texture";

//------------------------------------

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;


texture diffuseTexture : Diffuse
<
	string ResourceName = "default_color.dds";
>;

texture diffuseTexture2 : Diffuse;

//------------------------------------
struct vertexInput {
    float3 position				: POSITION;    
    float2 texCoordDiffuse		: TEXCOORD0;
    float4 data		: COLOR;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float2 texCoordDiffuse	: TEXCOORD0;
    float2 textureID	: TEXCOORD1;
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
    OUT.textureID.x =  IN.data.w;
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

sampler TextureSampler2 = sampler_state 
{
    texture = <diffuseTexture2>;
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
float4 diffuseTexture;
int ii = int(IN.textureID.x);
if(ii==0)
  diffuseTexture = tex2D( TextureSampler,IN.texCoordDiffuse);
else
 diffuseTexture = tex2D( TextureSampler2,IN.texCoordDiffuse);

return diffuseTexture;

}

float radio_s= 0;
//-----------------------------------
float4 PS_Textured2( vertexOutput IN): COLOR
{
float4 diffuseTexture;
diffuseTexture = tex2D( TextureSampler,IN.texCoordDiffuse)*radio_s+tex2D( TextureSampler2,IN.texCoordDiffuse)*(1-radio_s);
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
    
     pass p1 
    {				
		PixelShader  = compile ps_3_0 PS_Textured2();
    }
}